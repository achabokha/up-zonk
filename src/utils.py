import argparse
import yaml
import json
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
    parser.add_argument("--config",  default='./up-zonk.yaml', required=False)
    args = parser.parse_args()

    filename_w_ext = os.path.basename(args.model)
    filename, file_extension = os.path.splitext(filename_w_ext)

    model_file_name = args.model if file_extension == "yaml" else filename + ".yaml"
    print(model_file_name)

    with open(args.config) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    model_path = os.path.join(config["up"], model_file_name)
    with open(model_path) as f:
        model = yaml.load(f, Loader=yaml.FullLoader)

    return config, model
