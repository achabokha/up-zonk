import argparse
import json

from os import listdir
from os.path import join, basename, splitext

def pp_json(json_thing, sort=True, indents=4):
    if isinstance(json_thing, str):
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
def load_json(file_name):
    with open(file_name, "r") as template_config_file:
        return json.load(template_config_file)
def get_params():

    parser = argparse.ArgumentParser(description="Parameters")
    parser.add_argument("model")
    parser.add_argument("template")
    parser.add_argument("output", default='./output')
    args = parser.parse_args()
    model_file = args.model
    template_file_dir = args.template
    output_folder = args.output

    filename_w_ext = basename(model_file)
    filename, file_extension = splitext(filename_w_ext)

    template_files = [f for f in listdir(template_file_dir) if f.endswith(".mustache")]

    with open(model_file) as file:
        model = json.load(file)

    return filename, model, template_files, output_folder, template_file_dir
