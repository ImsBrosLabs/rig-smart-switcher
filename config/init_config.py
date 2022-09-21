import os
import yaml
from cerberus import Validator

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_config_file():
    config_file_path = os.path.join(BASE_DIR, 'config.yml')
    with open(config_file_path, 'r') as stream:
        try:
            return yaml.load(stream, Loader=yaml.FullLoader)
        except yaml.YAMLError as exception:
            raise exception

# Validating the config.yml with the schema defined in config_schema.py
schema = eval(open(os.path.join(BASE_DIR, 'config_schema.py'), 'r').read())

v = Validator(schema)
config_file = load_config_file()
is_valid = v.validate(config_file, schema)

if not is_valid:
    raise Exception('Invalid config.yml file', v.errors)
