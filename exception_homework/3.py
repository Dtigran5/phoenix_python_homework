import json

def parse_json_strings(json_strings):
    parsed_dicts = []
    for json_str in json_strings:
        try:
            parsed_dict = json.loads(json_str)
            parsed_dicts.append(parsed_dict)
        except json.JSONDecodeError as e:
            raise Exception(f'Error parsing JSON: {str(e)}')
    return parsed_dicts

json_strings = [
    '{"name": "John Doe", "age": 30, "city": "New York", "email": "johndoe@example.com", "is_student": false, "grades": [85, 90, 88]}'
]

parse_json_strings(json_strings) #valid json

json_strings1 = {
  "name": "John Doe",
  "age": 30,
  "city": "New York",
  "email": "johndoe@example.com",
  "is_student": False,
  "grades": [85, 90, 88]
}

parse_json_strings(json_strings1) #innvalid json