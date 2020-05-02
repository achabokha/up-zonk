import argparse
import json
import re
import os


def get_params():

    parser = argparse.ArgumentParser(description="Parameters")
    parser.add_argument("model")
    parser.add_argument("template")
    parser.add_argument("output", default='./output')
    args = parser.parse_args()
    modelFile = args.model
    templateFile = args.template
    outputFolder = args.output

    filename_w_ext = os.path.basename(modelFile)
    filename, file_extension = os.path.splitext(filename_w_ext)

    with open(modelFile) as f:
        model = json.load(f)

    template = open(templateFile, "r").read()

    return filename, model, template, outputFolder
