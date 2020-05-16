
import traceback
import pystache
import inflect
import names
from utils import load_json

class Genesis:
    def __init__(self, name, model, templates, output_folder, template_dir):
        self.name = name
        self.inflect = inflect.engine()
        self.model = self.__parse_model(model)
        self.templates = templates
        self.output_folder = output_folder
        self.template_dir = template_dir

    def create(self):
        for template_file in self.templates:
            print(f'Starting to render {template_file}')
            template = open(f'{self.template_dir}/{template_file}', "r").read()

            #pp_json(self.model)
            try:
                template_config = load_json(f'{self.template_dir}/{template_file}.json')
                output = pystache.render(template, self.model)
            except FileNotFoundError:
                print('Could not load template config')
                traceback.print_exc()
                continue

            file_name = template_config["outFileName"].replace("{name}", self.name)
            output_file_name = f'{self.output_folder}/{template_config["outDir"]}'
            output_file_name = output_file_name + f'/{file_name}'
            with open(output_file_name, "w") as output_file:
                output_file.write(output)

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
