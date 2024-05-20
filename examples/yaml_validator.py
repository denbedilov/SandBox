from jsonschema import validate, ValidationError
import yaml

schema = yaml.safe_load(open("yaml_validator/schema.yaml"))

configuration = yaml.safe_load(open("yaml_validator/sample.yaml"))

try:
    validate(configuration, schema)
    print("Validation is ok")
except ValidationError as ve:
    raise ve
