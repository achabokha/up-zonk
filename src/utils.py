import argparse
import json
from os import listdir
from os.path import isfile, join, basename, splitext

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
    modelFile = args.model
    templateFileDir = args.template
    outputFolder = args.output

    filename_w_ext = basename(modelFile)
    filename, file_extension = splitext(filename_w_ext)

    templateFiles = [f for f in listdir(templateFileDir) if isfile(join(templateFileDir, f))]

    with open(modelFile) as f:
        model = json.load(f)

    return filename, model, templateFiles, outputFolder, templateFileDir
