import os 

def get_cfg_path():
    module_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(module_dir,'.gitignore' ,'config.json')
    return json_file_path

CFG_PATH = get_cfg_path()