from jsonschema import validate, ValidationError
import yaml

_schema_path = "yaml_validator/schema.yaml"
_yaml_path = "yaml_validator/sample.yaml"

def validate_yaml(schema_path: str, yaml_path: str):
    '''
    validate a yaml file with given schema and returns a dict
    '''
    schema = yaml.safe_load(open(schema_path))
    yaml_file = yaml.safe_load(open(yaml_path))

    try:
        validate(yaml_file, schema)
        return yaml_file
    except ValidationError as ve:
        raise ve

print(validate_yaml(_schema_path, _yaml_path))