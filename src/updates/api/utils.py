from json import loads


def is_json(json_data):
    try:
        is_valid = loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid