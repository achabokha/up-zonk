
import traceback
import pystache
import inflect
import names
import os.path
from os import path
import utils
import shutil


class Genesis:
    def __init__(self, config, meta_model):
        self.name = meta_model['name']
        self.meta_model = meta_model
        self.base_out_dir = config['zonk']
        self.base_models_dir = config['up']
        self.base_templates_dir = config['templates']
        self.inflect = inflect.engine()

        model_filepath = path.join(
            self.base_models_dir, 'original', self.name + '.json')
        self.model = self.__parse_model(utils.load_json(model_filepath))

        # for debbugging --
        # if(path.exists(self.base_out_dir)):
        #     shutil.rmtree(self.base_out_dir,  ignore_errors=True)

    def create(self):

        self.__build_files()

        # self.__build_ng_components()

    # def __build_ng_componets(self):

    def __build_files(self):
        files = self.meta_model['templates']['files']
        # TODO: makes excludes work --
        # excludes = self.meta_model['templates']['exclude'] if 'exclude' in self.meta_model['templates'] else "dah"

        for file in files:
            filename = file['name']
            template_filename = filename + '.mustache'
            template_filepath = path.join(
                self.base_templates_dir, template_filename)
            out_filename = filename + '.ts'

            if "outFileName" in file:
                out_filename = file["outFileName"].replace("{name}", self.name)

            out_dir = path.join(self.base_out_dir, file['outDir'])

            self.__build_template(template_filepath, out_dir, out_filename)

    def __build_template(self, template_filepath, out_dir, out_filename):
        template = open(template_filepath, "r").read()
        out = pystache.render(template, self.model)

        if not path.exists(out_dir):
            os.makedirs(out_dir)

        out_filepath = path.join(out_dir, out_filename)
        with open(out_filepath, "w") as out_file:
            out_file.write(out)
            print(out_filepath)

    def __parse_model(self, model):
        model_fields = len(model)

        for i, item in enumerate(model):
            item["tsName"] = names.camelcase(item["COLUMN_NAME"])
            item['tsType'] = self.__mysql_to_ts_type(item["DATA_TYPE"])
            item['isPK'] = item['COLUMN_KEY'] == 'PRI'
            item['isRequired'] = item['IS_NULLABLE'] == 'NO'
            item['isLastField'] = (model_fields-1) == i

        new_model = {
            "name": names.pascalcase(self.name),
            "table": model[0]['TABLE_NAME'],
            "plural_name": self.inflect.plural(model[0]['TABLE_NAME']),
            "fields": model
        }
        return new_model

    def __mysql_to_ts_type(self, field_type):
        map_types = {
            "tinyint": "number",
            "int": "number",
            "decimal": "number",
            "varchar": "string",
            "char": "string",
            "datetime": "string",
            "text": "string",
            "bit": "boolean"
        }
        return map_types[field_type]
