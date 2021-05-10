
import names
import re


class MySQL:
    def __init__(self, meta_model, model):
        self.name = meta_model['name']
        self.meta_model = meta_model
        self.model = model

    def parse(self):

        model_fields = len(self.model)

        for i, item in enumerate(self.model):
            field_name = item["COLUMN_NAME"]
            item["tsName"] = names.camelcase(field_name)
            item["camelName"] = names.camelcase(field_name)
            item["capitalName"] = self.__sanitize_name(names.capitalcase(
                names.spacecase(field_name)))

            item['tsType'] = self.__mysql_to_ts_type(item["DATA_TYPE"])
            item['isPK'] = item['COLUMN_KEY'] == 'PRI'
            item['isAutoIncrement'] = item['EXTRA'] == 'auto_increment'
            item['isID'] = item['isPK'] or item['isAutoIncrement']
            item['isDisplay'] = False if item['isID'] else self.__is_field(
                field_name)
            item['isRequired'] = item['IS_NULLABLE'] == 'NO'
            item['isReadOnly'] = self.__is_readonly(item)
            item['isListLink'] = self.__is_list_link(item)
            item['controlType'] = self.__mysql_to_control_type(item)
            item['isToggle'] = item['controlType'] == 'toggle'
            item['isInput'] = item['controlType'] == 'input'
            item['isTextbox'] = item['controlType'] == 'textbox'
            item['inputType'] = item['tsType']
            item['maxLength'] = item["CHARACTER_MAXIMUM_LENGTH"]

            if item['controlType'] == 'toggle':
                item["itemTemplateExpr"] = "{{ item." + \
                    names.camelcase(field_name) + \
                    " == '1'? 'yes' : 'no'" + " }}"
            else:
                item["itemTemplateExpr"] = "{{ item." + \
                    names.camelcase(field_name) + " }}"

            item['isFirstField'] = i == 0
            item['isLastField'] = (model_fields-1) == i

        new_model = {
            "name": self.name,
            "kebabName": self.name,
            "kebabNamePlural": names.plural(self.name),
            "pascalName": names.pascalcase(self.name),
            "pascalNamePlural": names.pascalcase(names.plural(self.name)),
            "camelName": names.camelcase(self.name),
            "camelNamePlural": names.camelcase(names.plural(self.name)),
            "capitalName": names.capitalcase(names.spacecase(self.name)),
            "spaceName": names.spacecase(self.name),

            "table": self.model[0]['TABLE_NAME'],

            "fields": self.model
        }

        if 'params' in self.meta_model:
            params = self.meta_model['params']
            new_model = {**new_model, **params}

        # utils.pp_json(new_model)

        return new_model

    def __mysql_to_ts_type(self, field_type):
        map_types = {
            "tinyint": "number",
            "smallint": "number",
            "int": "number",
            "decimal": "number",
            "double": "number",
            "varchar": "string",
            "char": "string",
            "datetime": "string",
            "text": "string",
            "longtext": "string",
            "bit": "boolean"
        }
        return map_types[field_type]

    def __mysql_to_control_type(self, item):
        if item["COLUMN_NAME"] == 'active_ind':
            return 'toggle'

        if item["DATA_TYPE"] == 'text':
            return 'textbox'

        if item["DATA_TYPE"] == 'longtext':
            return 'textbox'

        max_length = item['CHARACTER_MAXIMUM_LENGTH']
        if max_length is None:
            return 'input'

        return 'input' if max_length <= 128 else 'textbox'

    def __sanitize_name(self, string):
        # TODO: need a better matching. Need a loop, exit with a first found.
        words = {
            'desc': 'description',
            'expr': 'expression',
            'seq': 'sequence',
            'num': 'number',
            'Num': 'Number of',
            'ind': '',
        }
        return re.sub(r'\w+', lambda x: words.get(x.group(), x.group()), string)

    def __is_field(self, field_name):
        no_fields = [
            'created_date_time',
            'updated_date_time',
            'step_seq_num'
        ]
        return not field_name in no_fields

    def __is_readonly(self, item):
        field_name = item["COLUMN_NAME"]
        link_names = [
            "name"
        ]
        return field_name in link_names

    def __is_list_link(self, item):
        field_name = item["COLUMN_NAME"]
        link_names = [
            "name"
        ]
        return field_name in link_names
