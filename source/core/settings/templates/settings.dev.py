# mypy: ignore-errors

SECRET_KEY = "django-insecure-_f27t##y1uo-5&69sdn*py--mm=9-_l5xb(*y=#ksa)g-$o#up"

DEBUG = True

LOGGING["formatters"]["colored"] = {  # type: ignore # noqa: F821
    "()": "colorlog.ColoredFormatter",
    "format": "%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s",
}
LOGGING["loggers"]["core"]["level"] = "DEBUG"  # type: ignore # noqa: F821
LOGGING["handlers"]["console"]["level"] = "DEBUG"  # type: ignore # noqa: F821
LOGGING["handlers"]["console"]["formatter"] = "colored"  # type: ignore # noqa: F821
