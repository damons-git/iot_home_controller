def raw_string(input_str: str):
    raw = r"{}".format(input_str)
    return raw


def valid_json(self, value: str) -> bool:
    # Guard to check that string provided is parsable JSON
    try:
        json.loads(value)
        return True

    except ValueError:
        return False

    except Exception as err:
        print(err)
        return False