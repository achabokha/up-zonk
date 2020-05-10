import sys
from utils import get_params
from genesis import Genesis

print("Welcome to Up-Zonk, a Code Generation!")
print("[DEBUG] Python version: ", sys.version)

name, model, template, output_folder, template_dir = get_params()
print(f'Model used {name}.js')

Genesis(name, model, template[:1], output_folder, template_dir).create()
