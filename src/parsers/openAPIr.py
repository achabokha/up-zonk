
import names
import re

class openAPIr:
    def __init__(self, meta_model, model):
        self.name = meta_model['name']
        self.meta_model = meta_model
        self.model = model

    def parse(self):
        model = self.model
