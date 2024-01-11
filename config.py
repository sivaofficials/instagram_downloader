import json

def get_config(key):
    config_file="config.json"
    with open(config_file) as file:
        config=json.load(file)
        file.close()
    
    if key in config:
        return config[key]
    else:
        raise Exception('key not fond')