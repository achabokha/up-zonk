import traceback
import os.path as path
import os
import shutil
import pystache
import names
import utils
import re


class Genesis:
    def __init__(self, config, meta_model):
        self.name = meta_model['name']
        self.meta_model = meta_model
        self.base_out_dir = config['zonk']
        self.base_models_dir = config['up']
        self.base_templates_dir = config['templates']

        model_filepath = path.join(
            self.base_models_dir, 'original', self.name + '.json')
        self.model = self.__parse_model(utils.load_json(model_filepath))

        # for debbugging --
        # if(path.exists(self.base_out_dir)):
        #     shutil.rmtree(self.base_out_dir,  ignore_errors=True)

    def create(self):

        self.__build_files()

        self.__build_ng_components()

    def __build_files(self):
        files = self.meta_model['templates']['files']
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

            out_filename = out_filename + '.' + filename + '.ts'

            if "outFileName" in file:
                out_filename = file["outFileName"].replace(
                    "{name}", self.name)

            out_dir = path.join(self.base_out_dir, file['outDir'])

            self.__build_template(template_filepath, out_dir, out_filename)

    def __build_ng_components(self):
        ng_components = self.meta_model['templates']['ngComponents']
        components_out_dir = self.meta_model['templates']['ngComponentsOutDir']

        excludes = []
        if 'exclude' in self.meta_model['templates']:
            if 'ngComponents' in self.meta_model['templates']['exclude']:
                excludes = self.meta_model['templates']['exclude']['ngComponents']

        for component in ng_components:
            if excludes and component in excludes:
                continue

            html_template_filepath = path.join(
                self.base_templates_dir, component, 'component.html.mustache')
            scss_template_filepath = path.join(
                self.base_templates_dir, component, 'component.scss.mustache')
            ts_template_filepath = path.join(
                self.base_templates_dir, component, 'component.ts.mustache')

            component_name = self.name + '-' + component
            html_out_filepath = component_name + '.component.html'
            scss_out_filepath = component_name + '.component.scss'
            ts_out_filepath = component_name + '.component.ts'

            out_dir = path.join(
                self.base_out_dir, components_out_dir, component_name)

            self.__build_template(html_template_filepath,
                                  out_dir, html_out_filepath)
            self.__build_template(scss_template_filepath,
                                  out_dir, scss_out_filepath)
            self.__build_template(ts_template_filepath,
                                  out_dir, ts_out_filepath)

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

    def __parse_model(self, model):
        model_fields = len(model)

        for i, item in enumerate(model):
            field_name = item["COLUMN_NAME"]
            item["tsName"] = names.camelcase(field_name)
            item["camelName"] = names.camelcase(field_name)
            item["capitalName"] = self.__sanitize_name(names.capitalcase(
                names.spacecase(field_name)))
            item["itemTemplateExpr"] = "{{ item." + \
                names.camelcase(field_name) + "}}"

            item['tsType'] = self.__mysql_to_ts_type(item["DATA_TYPE"])
            item['isPK'] = item['COLUMN_KEY'] == 'PRI'
            item['isAutoIncrement'] = item['EXTRA'] == 'auto_increment'
            item['isID'] = item['isPK'] or item['isAutoIncrement']
            item['isDisplay'] = False if item['isID'] else self.__is_field(
                field_name)
            item['isReadOnly'] = field_name == 'name'
            item['isRequired'] = item['IS_NULLABLE'] == 'NO'
            item['controlType'] = self.__mysql_to_control_type(
                item['CHARACTER_MAXIMUM_LENGTH'])
            item['inputType'] = item['tsType']
            item['maxLength'] = item["CHARACTER_MAXIMUM_LENGTH"]

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

    def __mysql_to_control_type(self, max_length):
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
        }
        return re.sub(r'\w+', lambda x: words.get(x.group(), x.group()), string)

    def __is_field(self, field_name):
        no_fields = [
            'created_date_time',
            'updated_date_time',
            'step_seq_num'
        ]
        return not field_name in no_fields
