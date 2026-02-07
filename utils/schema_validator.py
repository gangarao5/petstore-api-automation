from jsonschema import validate
from jsonschema.exceptions import ValidationError

def validate_schema(response_json, schema):
    try:
        validate(instance=response_json, schema=schema)
        return True, None
    except ValidationError as e:
        return False, str(e)
