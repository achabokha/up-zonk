import sys
import utils
from genesis import Genesis

print("Welcome to Angular with Material Code Generation!")
print("[DEBUG] Python version: ", sys.version)

config, meta_model = utils.get_params()

### Debugging ####
# utils.pp_json(meta_model)
# utils.pp_json(config)

print('\nGenie-ing:\n')
print(meta_model['name'], '\n')
Genesis(config, meta_model).create()
print()
