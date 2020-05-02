import pystache
import names
import string


class Genesis:
    def __init__(self, name, model, template, output_folder):
        self.name = name
        self.model = self.__parse_model(model)
        self.template = template
        self.output_folder = output_folder

    def create(self):
        output = pystache.render(self.template, self.model)

        output_file_name = f'{self.output_folder}/{self.name}.ts'

        # print(output)

        with open(output_file_name, "w") as output_file:
            output_file.write(output)

    def __parse_model(self, model):
        l = len(model)

        for i, item in enumerate(model):
            item["tsName"] = names.camelcase(item["COLUMN_NAME"])
            item['tsType'] = self.__mysql_to_ts_type(item["DATA_TYPE"])
            item['isPK'] = item['COLUMN_KEY'] == 'PRI'
            item['isRequired'] = item['IS_NULLABLE'] == 'NO'
            item['isLastField'] = (l-1) == i

        new_model = {
            "name": names.pascalcase(self.name),
            "table": model[0]['TABLE_NAME'],
            "fields": model
        }
        return new_model

    def __mysql_to_ts_type(self, field_type):
        map = {
            "tinyint": "number",
            "int": "number",
            "decimal": "number",
            "varchar": "string",
            "char": "string",
            "datetime": "string",
            "text": "string",
            "bit": "boolean"
        }
        return map[field_type]
