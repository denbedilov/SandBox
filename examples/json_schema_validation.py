import json
import copy
from jsonschema import validate
from jsonschema.exceptions import ValidationError

schema = {}
schema_file = json.load(open("schema.json", "r"))
for schema_type in schema_file["schemas"]:
    schema[schema_type] = copy.copy(schema_file["schemas"][schema_type])
    schema[schema_type]["structs"] = schema_file["structs"]


box_data = {"box": "101"}
try:
    validate(box_data, schema["box_schema"])
    print("Schema is valid")
except ValidationError as e:
    print("Schema is invalid")
    print(e)
