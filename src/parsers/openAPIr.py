
import re
import names

class OpenAPIr:
    def __init__(self, meta_model, model):
        self.name = meta_model['name']
        self.meta_model = meta_model
        self.model = model

    def parse(self):

        table_name = list(self.model.keys())[0]

        fields = self.model[table_name]['properties']

        model_fields = len(fields)

        for i, field_name in enumerate(fields):
            item = fields[field_name]
            item["tsName"] = names.camelcase(field_name)
            item["camelName"] = names.camelcase(field_name)
            item["capitalName"] = self.__sanitize_name(names.capitalcase(
                names.spacecase(field_name)))

            item['tsType'] = item['type']
            item['format'] = 'format' in item
            
            item['isPK'] = field_name == "id"
            item['isAutoIncrement'] = field_name == "id"
            item['isID'] = field_name == "id"

            item['isDisplay'] = False if item['isID'] else self.__is_field(
                field_name)
            item['isRequired'] = False
            item['isReadOnly'] = False
            item['isListLink'] = field_name == "id"
            item['controlType'] = self.__to_control_type(item)
            item['isToggle'] = item['controlType'] == 'toggle'
            item['isInput'] = item['controlType'] == 'input'
            item['isTextbox'] = item['controlType'] == 'textbox'
            item['inputType'] = item['tsType']
            item['maxLength'] = None
            item['info'] = item['description'] if 'description' in item.keys() else item['capitalName']
            item['COLUMN_NAME'] = names.underscorecase(field_name)

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
            "pascalNameO": names.pascalcase(self.name),
            "pascalName": names.nospacescase(names.pascalcase(self.__sanitize_name(names.spacecase(self.name)))),
            "pascalNamePlural": names.pascalcase(names.plural(self.name)),
            "camelName": names.camelcase(self.name),
            "camelNamePlural": names.camelcase(names.plural(self.name)),
            "capitalName": self.__sanitize_name(names.capitalcase(names.spacecase(self.name))),
            # "capitalName": names.capitalcase(names.spacecase(self.name)),
            "spaceName": names.spacecase(self.name),

            "table": names.underscorecase(table_name),

            "fields": list(fields.values())
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
            'desc': 'description',
            'expr': 'expression',
            'seq': 'sequence',
            'num': 'number',
            'Num': 'Number of',
            'ind': '',
        }
        return re.sub(r'\w+', lambda x: words.get(x.group(), x.group()), string)
    
    def __to_control_type(self, item):
        controls = {
            'number': 'input',
            'string': 'input',
            'boolean': 'toggle'
        }

        return controls[item['type']]
    
    def __is_field(self, field_name):
        no_fields = [
            'created_date_time',
            'updated_date_time',
            'step_seq_num'
        ]
        return not field_name in no_fields


