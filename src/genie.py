import sys
<<<<<<< HEAD
import os
import json
import utils
=======
from utils import get_params
>>>>>>> ba349a12e18f6b81047933d6a393e88fad120c1d
from genesis import Genesis


print("Welcome to Up-Zonk, a Code Generation!")
# print("[DEBUG] Python version: ", sys.version)

config, model = utils.get_params()
print("Config:")
json.dump(config, sys.stdout, indent=4)
print()
print("Model: ")
json.dump(model, sys.stdout, indent=4)

<<<<<<< HEAD


# Genesis(name, model, template, output_folder).create()
=======
name, model, template, output_folder, template_dir = get_params()
print(f'Model used {name}.js')

Genesis(name, model, template, output_folder, template_dir).create()
>>>>>>> ba349a12e18f6b81047933d6a393e88fad120c1d
