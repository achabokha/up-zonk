import argparse
import yaml
import json
import re
import os


def get_params():

    parser = argparse.ArgumentParser(description="Parameters")
    parser.add_argument("config", default='./up-zonk.yaml')
    parser.add_argument("model")
    args = parser.parse_args()

    with open(args.config) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    model_path = os.path.join(config["up"], args.model)
    with open(model_path) as f:
        model = yaml.load(f, Loader=yaml.FullLoader)

    return config, model
