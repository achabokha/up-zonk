import sys
import utils
from genesis import Genesis

print("Welcome to Up-Zonk, a Code Generation!")
# print("[DEBUG] Python version: ", sys.version)

config, meta_model = utils.get_params()

print('\nGenerated:\n')
Genesis(config, meta_model).create()
print()
