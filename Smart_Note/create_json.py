import json
import os

def write_json(name_file, data):
    abs_path = os.path.abspath(__file__ + "/..")
    os.chdir(abs_path)
    with open(os.path.join(abs_path, name_file), "w", encoding= "utf-8") as file:
        json.dump(data, file, indent=4,ensure_ascii= False)
def read_json(name_file):
    abs_path = os.path.abspath(__file__ + "/..")
    with open(os.path.join(abs_path, name_file), "r", encoding= "utf-8") as file:
        data = json.load(file)
    return(data)    
