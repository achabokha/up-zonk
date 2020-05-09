import pystache
import names

class Genesis:
    def __init__(self, name, model, templates, output_folder, template_dir):
        self.name = name
        self.model = self.__parse_model(model)
        self.templates = templates
        self.output_folder = output_folder
        self.template_dir = template_dir

    def create(self):
        for template_file in self.templates:
            print(f'Starting to render {template_file}')
            template = open(f'{self.template_dir}/{template_file}', "r").read()
            output = pystache.render(template, self.model)

            file_name = template_file.replace('.mustache', '')
            output_file_name = f'{self.output_folder}/{file_name}.ts'
            # print(output)

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
