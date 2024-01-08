from source.core.utils.collections import update_conf
from source.core.utils.settings import get_settings_from_env

update_conf(globals(), get_settings_from_env(ENV_SETTINGS_PREFIX))  # type: ignore # noqa: F821
