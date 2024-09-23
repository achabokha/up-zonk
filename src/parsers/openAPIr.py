
import re
import names
import utils

class OpenAPIr:
    def __init__(self, meta_model, model_filepath_base):
        self.name = meta_model['name']
        self.meta_model = meta_model
        self.model_filepath_base = model_filepath_base
       
    def parse(self, model: object = None):     
        if model is None:
            model = utils.load_yaml(self.model_filepath_base + '.yaml')
    
        self.model = model
        model_name = list(self.model.keys())[0]

        fields = self.model[model_name]['properties']
        description = self.model[model_name]['description'] if 'description' in self.model[model_name].keys() else model_name

        model_fields = len(fields)

        for i, field_name in enumerate(fields):
            item = fields[field_name]
            item["tsName"] = names.camelcase(field_name)
            item["camelName"] = names.camelcase(field_name)
            item["capitalName"] = self.__sanitize_name(names.capitalcase(names.spacecase(field_name)))
            item["titleCase"] = self.__sanitize_name((names.spacecase(field_name))).title()

            item['tsType'] = item['type']
            item['isRequired'] = item.get('required')
            item['format'] = item.get('format')

            item['isPK'] = field_name == "id"
            item['isAutoIncrement'] = field_name == "id"
            item['isID'] = field_name == "id"

            item['isDisplay'] = False if item['isID'] else self.__is_field(field_name)
            item['isListLink'] = self.__is_list_link(field_name)
            item['controlType'] = self.__to_control_type(item)
            item['isToggle'] = item['controlType'] == 'toggle'
            item['isInput'] = item['controlType'] == 'input'
            item['isTextbox'] = item['controlType'] == 'textbox'
            item['isNumber'] = item['tsType'] == 'number'

            item['inputType'] = item['tsType']
            item['maxLength'] = None
            item['info'] = item['description'] if 'description' in item.keys() else item['capitalName']
            item['dbColumnName'] = names.underscorecase(field_name)
            item['dbColumnType'] = self.__type_to_mysql(item["type"], item["format"])

            if item['controlType'] == 'toggle':
                item["itemTemplateExpr"] = "{{ item." + \
                    names.camelcase(field_name) + \
                    " == '1'? 'yes' : 'no'" + " }}"
            elif item["format"]:
                map_1 = {
                    "date": "{{ item." + names.camelcase(field_name) + " | df: \"date\" }}",
                    "date-time": "{{ item." + names.camelcase(field_name) + " | df }}",
                }
                item["itemTemplateExpr"] = map_1[item["format"]]
                item["cssClass"] = item["format"]
            elif item["type"] == "number":
                item["itemTemplateExpr"] = "{{ item." + \
                    names.camelcase(field_name) + " | number }}"
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
            "capitalNamePlural": self.__sanitize_name(names.capitalcase(names.spacecase(names.plural(self.name)))),
            "spaceName": names.spacecase(self.name),

            "table": names.underscorecase(model_name),
            "title": description,
            "titleCase": self.__sanitize_name((names.spacecase(self.name))).title(),
            "titleCasePlural":  self.__sanitize_name((names.spacecase(names.plural(self.name)))).title(),

            "fields": list(fields.values())
        }

        if 'params' in self.meta_model:
            params = self.meta_model['params']
            new_model = {**new_model, **params}

        ## debug dump to console --
        # utils.pp_json(new_model)

        return new_model

    def __sanitize_name(self, string):
        # TODO: need a better matching. Need a loop, then exit with a first found.
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

    def __to_control_type(self, item):
        controls = {
            'number': 'input',
            'string': 'input',
            'boolean': 'toggle'
        }

        return controls[item['type']]

    def __is_field(self, field_name):
        no_fields = [
            'created-date-time',
            'updated-date-time',
            'seq-num'
        ]
        return not field_name in no_fields

    def __type_to_mysql(self, i_type, i_format):

        if i_format:
            map_1 = {
                "date": "date DEFAULT NULL",
                "date-time": "datetime DEFAULT NULL",
            }
            return map_1[i_format]

        map_2 = {
            "number": "int DEFAULT 0",
            "string": "varchar(255) DEFAULT NULL",
        }
        return map_2[i_type]

    def __is_list_link(self, field_name):
        link_names = [
            "name"
        ]
        return field_name in link_names
