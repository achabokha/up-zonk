
import re
import names


class Athena:
    def __init__(self, meta_model, model):
        self.name = meta_model['name']
        self.meta_model = meta_model
        self.model = model

    def parse(self):

        table_name = self.name
        fields = self.model
        model_field_count = len(fields)

        for i, item in enumerate(fields):
            field_name = item["Name"]

            item["tsName"] = names.camelcase(field_name)
            item["camelName"] = names.camelcase(field_name)
            item["capitalName"] = self.__sanitize_name(names.capitalcase(
                names.spacecase(field_name)))

            field_type = item['Type']
            item['tsType'] = self.__to_ts_type(field_type)
            # item['format'] = item.get('format')

            item['isPK'] = field_name == "id"
            item['isAutoIncrement'] = field_name == "id"
            item['isID'] = field_name == "id"

            item['isDisplay'] = False if item['isID'] else self.__is_field(
                field_name)
            item['isRequired'] = False
            item['isReadOnly'] = False
            item['isListLink'] = field_name == "id"

            # type html control
            item['controlType'] = self.__to_control_type(field_type)
            item['isToggle'] = item['controlType'] == 'toggle'
            item['isInput'] = item['controlType'] == 'input'
            item['isTextbox'] = item['controlType'] == 'textbox'
            item['isNumber'] = item['tsType'] == 'number'

            item['inputType'] = item['tsType']
            item['maxLength'] = None
            item['info'] = item['capitalName']
            item['COLUMN_NAME'] = names.underscorecase(field_name)
            item['COLUMN_TYPE'] = self.__type_to_mysql(field_type)

            if item['controlType'] == 'toggle':
                item["itemTemplateExpr"] = "{{ item." + \
                    names.camelcase(field_name) + \
                    " == '1'? 'yes' : 'no'" + " }}"
            elif field_type == "number":
                item["itemTemplateExpr"] = "{{ item." + \
                    names.camelcase(field_name) + " | number }}"
            else:
                item["itemTemplateExpr"] = "{{ item." + \
                    names.camelcase(field_name) + " }}"

            item['isFirstField'] = i == 0
            item['isLastField'] = (model_field_count-1) == i

        new_model = {
            "name": self.name,
            "kebabName": self.name,
            "kebabNamePlural": names.plural(self.name),
            "pascalNameO": names.pascalcase(self.name),
            "pascalName": names.nospacescase(names.pascalcase(self.__sanitize_name(names.spacecase(self.name)))),
            "pascalNamePlural": names.pascalcase(names.plural(self.name)),
            "camelName": names.camelcase(self.name),
            "camelNamePlural": names.camelcase(names.plural(self.name)),
            "capitalName": self.__sanitize_name(names.capitalcase(names.spacecase(self.name))),
            # "capitalName": names.capitalcase(names.spacecase(self.name)),
            "spaceName": names.spacecase(self.name),

            "table": names.underscorecase(table_name),
            # "title": description,``

            "fields": self.model
        }

        if 'params' in self.meta_model:
            params = self.meta_model['params']
            new_model = {**new_model, **params}

        # utils.pp_json(new_model)

        return new_model

    def __sanitize_name(self, string):
        # TODO: need a better matching. Need a loop, exit with a first found.
        words = {
            'api': 'API',
            'cpu': "CPU",
            'desc': 'description',
            'expr': 'expression',
            'seq': 'sequence',
            'num': 'number',
            'Num': 'Number of',
            'ind': '',
        }
        return re.sub(r'\w+', lambda x: words.get(x.group(), x.group()), string)

    def __to_ts_type(self, field_type):
        map_types = {
            "bigint": "number",
            "varchar": "string",
        }
        return map_types[field_type]

    def __to_control_type(self, field_type):
        controls = {
            'varchar': 'input',
            'bigint': 'input',
        }

        return controls[field_type]

    def __is_field(self, field_name):
        no_fields = [
            'created-date-time',
            'updated-date-time',
            'step-seq-num'
        ]
        return not field_name in no_fields

    def __type_to_mysql(self, i_type):
        types = {

            "bigint": "int DEFAULT 0",
            "varchar": "varchar(255) DEFAULT NULL",
        }
        return types[i_type]
