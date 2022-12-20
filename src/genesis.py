# import sys
# import traceback
import os.path as path
import os
# import re
# import shutil
import pystache
import names
from parsers.athena import Athena
import utils

from parsers.MySQL import MySQL
from parsers.openAPIr import OpenAPIr
from parsers.athena import Athena

class Genesis:
    def __init__(self, config, meta_model):
        self.name = meta_model['name']
        self.meta_model = meta_model
        self.base_out_dir = config['zonk']
        self.base_models_dir = config['up']
        self.base_templates_dir = config['templates']

        model_filepath_base = path.join(
            self.base_models_dir, self.meta_model['modelType'], self.name)

        if(path.exists(model_filepath_base + '.json')):
            original_model = utils.load_json(model_filepath_base + '.json')
        elif path.exists(model_filepath_base + '.yaml'):
            original_model = utils.load_yaml(model_filepath_base + '.yaml')
        else: 
            raise Exception(f'Json or Yaml model files are not found for model [{model_filepath_base}]')  
        
        print(f'Model [{model_filepath_base}] found!')

        parsers = {
            'mysql': MySQL(meta_model, original_model),
            'open-api-r': OpenAPIr(meta_model, original_model),
            'athena': Athena(meta_model, original_model)
        }

        parser = parsers[meta_model['modelType']]
        self.model = parser.parse()

        # for debbugging --
        # if(path.exists(self.base_out_dir)):
        #     shutil.rmtree(self.base_out_dir,  ignore_errors=True)

    def create(self):

        self.__build_files()

        self.__build_ng_components()

    def __build_files(self):
        if 'files' in self.meta_model['templates']:
            files = self.meta_model['templates']['files']
        else:
            return

        excludes = []
        if 'exclude' in self.meta_model['templates']:
            if 'files' in self.meta_model['templates']['exclude']:
                excludes = self.meta_model['templates']['exclude']['files']

        for file in files:
            filename = file['name']
            if excludes and filename in excludes:
                continue

            template_filename = filename + '.mustache'
            template_filepath = path.join(
                self.base_templates_dir, template_filename)

            out_filename = self.name
            if "outFileNamePlural" in file:
                if file["outFileNamePlural"]:
                    out_filename = names.plural(out_filename)

            out_filename = out_filename + '.' + filename

            if "outFileName" in file:
                out_filename = file["outFileName"].replace(
                    "{name}", self.name)

            out_dir = path.join(self.base_out_dir, file['outDir'])

            self.__build_template(template_filepath, out_dir, out_filename)

    def __build_ng_components(self):
        if 'ngComponents' in self.meta_model['templates']:
            ng_components = self.meta_model['templates']['ngComponents']
        else:
            return

        components_out_dir = self.meta_model['templates']['ngComponentsOutDir']

        excludes = []
        if 'exclude' in self.meta_model['templates']:
            if 'ngComponents' in self.meta_model['templates']['exclude']:
                excludes = self.meta_model['templates']['exclude']['ngComponents']

        for component in ng_components:
            if excludes and component in excludes:
                continue

            for file_name in os.listdir(path.join(self.base_templates_dir, component)):

                if file_name.startswith('--'):
                    continue

                template_filepath = path.join(
                    self.base_templates_dir, component, file_name)

                out_filepath = self.name + '-' + component + \
                    '.' + file_name.replace('.mustache', '')

                component_name = self.name + '-' + component

                out_dir = path.join(
                    self.base_out_dir, components_out_dir, component_name)

                self.__build_template(template_filepath, out_dir, out_filepath)

    def __build_template(self, template_filepath, out_dir, out_filename):

        template = open(template_filepath, "r").read()
        out = pystache.render(template, self.model)

        if not path.exists(out_dir):
            # TODO: sometimes threw an exception when out_dir is empty,
            # no idea why --
            os.makedirs(out_dir)

        out_filepath = path.join(out_dir, out_filename)
        with open(out_filepath, "w") as out_file:
            out_file.write(out)
            print(out_filepath)
