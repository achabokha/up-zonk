import argparse
import json
import yaml
import os
from os.path import join, basename, splitext


def pp_json(json_thing, sort=True, indents=4):
    if isinstance(json_thing, str):
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))


def load_json(file_name):
    with open(file_name, "r") as file_stream:
        return json.load(file_stream)

def load_yaml(file_name):
    with open(file_name, "r") as file_stream:
        return yaml.load(file_stream, Loader=yaml.FullLoader)

def get_params():

    parser = argparse.ArgumentParser(description="Parameters")
    parser.add_argument("meta_model")
    parser.add_argument("--config",  default='./up-zonk.yaml', required=False)
    args = parser.parse_args()

    config = load_yaml(args.config)

    # meta model load, can be without .yaml ext --
    filename_w_ext = os.path.basename(args.meta_model)
    filename, file_extension = os.path.splitext(filename_w_ext)

    meta_model_file_name = args.model if file_extension == "yaml" else filename + ".yaml"

    meta_model_path = os.path.join(config["up"], meta_model_file_name)
    meta_model = load_yaml(meta_model_path)

    return config, meta_model
