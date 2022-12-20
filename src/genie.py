import sys
import utils
from genesis import Genesis

print("Welcome to Up-Zonk, a Code Generation!")
# print("[DEBUG] Python version: ", sys.version)

config, meta_model = utils.get_params()

# utils.pp_json(meta_model)
# utils.pp_json(config)

print('\nGenie-ing:\n')
print(meta_model['name'], '\n')
Genesis(config, meta_model).create()
print()
