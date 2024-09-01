import pandas as pd

from parsers.openAPIr import OpenAPIr


class Csv:
    def __init__(self, meta_model, model_filepath_base):
        self.name = meta_model['name']
        self.meta_model = meta_model
        self.model_filepath_base = model_filepath_base
    
    def parse(self):
        # model_name = list(self.model.keys())[0]
        df = pd.read_csv(self.model_filepath_base + '.csv')

        properties = {}
        for val in df.values:
            properties[val[0]] = {}
            properties[val[0]]["type"] = val[1]
            if not pd.isna(val[2]): properties[val[0]]["format"] = val[2]
            if not pd.isna(val[3]): properties[val[0]]["description"] = val[3]
        
        self.model = {
            self.name: {
                "properties": properties,
            }
        }
        
    
        """ Let's turn CSV data to OpenAPIr model and then run the OpenAPIr parser """
        return OpenAPIr(self.meta_model, self.model_filepath_base).parse(self.model)
        
        