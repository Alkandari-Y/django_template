def update_conf(base_config, new_config):
    for key, value in new_config.items():
        if isinstance(value, dict):
            base_config_value = base_config.get(key)

            if isinstance(base_config_value, dict):
                update_conf(base_config_value, value)
            else:
                base_config[key] = value
        else:
            base_config[key] = value

    return base_config
