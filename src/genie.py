import sys
import json
import utils
from genesis import Genesis


print("Welcome to Up-Zonk, a Code Generation!")
# print("[DEBUG] Python version: ", sys.version)

config, model = utils.get_params()
print("Config:")
json.dump(config, sys.stdout, indent=4)
print()
print("Model: ")
json.dump(model, sys.stdout, indent=4)



# Genesis(name, model, template, output_folder).create()
