import argparse
import json
import re
from os import listdir
from os.path import isfile, join, basename, splitext

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
