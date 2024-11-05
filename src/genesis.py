
import os.path as path
import os
import pystache

import names

from parsers.openAPIr import OpenAPIr
from parsers.csv import Csv


class Genesis:
    def __init__(self, config, meta_model):
        self.name = meta_model['name']
        self.meta_model = meta_model
        self.base_out_dir = config['output']
        self.base_models_dir = config['models']
        self.base_templates_dir = config['templates']

        model_filepath_base = path.join(self.base_models_dir, self.meta_model['modelType'], self.name)

        parsers = {
            'open-api-r': OpenAPIr(meta_model, model_filepath_base),
            'csv': Csv(meta_model, model_filepath_base),
            ## TODO: add update parsers for below model types
            # 'mysql': MySQL(meta_model, model_filepath_base),
            # 'athena': Athena(meta_model, model_filepath_base)
        }

        parser = parsers[meta_model['modelType']]
        self.model = parser.parse()

        # for debugging --
        # if(path.exists(self.base_out_dir)):
        #     shutil.rmtree(self.base_out_dir, ignore_errors=True)

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
            # adding logic to split component name if there is a hypen in the name 
            # and use the word after hypen as part of component name
            cmpArr = component.split(" ")
            if len(cmpArr) > 1:
                component = cmpArr[0]
                componentRename = cmpArr[1]
            else:
                componentRename = component
            if excludes and component in excludes:
                continue

            for file_name in os.listdir(path.join(self.base_templates_dir, component)):

                if file_name.startswith('--'):
                    continue
          
                template_filepath = path.join(
                    self.base_templates_dir, component, file_name)

                out_filepath = self.name + '-' + componentRename + \
                    '.' + file_name.replace('.mustache', '')

                component_name = self.name + '-' + componentRename
              
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
