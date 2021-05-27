
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
            item['isPK'] = False
            item['isAutoIncrement'] = False
            item['isID'] = False
            item['isDisplay'] = False if item['isID'] else True
            item['isRequired'] = False
            item['isReadOnly'] = False
            item['isListLink'] = False
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
            "pascalName": names.pascalcase(self.name),
            "pascalNamePlural": names.pascalcase(names.plural(self.name)),
            "camelName": names.camelcase(self.name),
            "camelNamePlural": names.camelcase(names.plural(self.name)),
            "capitalName": names.capitalcase(names.spacecase(self.name)),
            "spaceName": names.spacecase(self.name),

            "table": table_name,

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

