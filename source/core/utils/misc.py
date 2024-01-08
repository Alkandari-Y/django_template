import yaml


def yaml_coerce(value):
    if isinstance(value, str):
        return yaml.load(f"val: {value}", Loader=yaml.SafeLoader)["val"]

    return value
