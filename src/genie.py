import sys
import os
from utils import get_params
from genesis import Genesis

print("Welcome to Up-Zonk, a Code Generation!")
print("[DEBUG] Python version: ", sys.version)

name, model, template, output_folder = get_params()
print(name)

Genesis(name, model, template, output_folder).create()

