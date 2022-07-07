import json
import os


def plugin_settings(settings):
    DEREX_PROJECT = os.environ.get("DEREX_PROJECT")

    settings.LEARNING_MICROFRONTEND_URL = os.environ.get(
        "DEREX_LEARNING_MICROFRONTEND_URL",
        "http://learning.{}.localhost".format(DEREX_PROJECT),
    )

    LEARNING_MICROFRONTEND_ALIASES = os.environ.get(
        "DEREX_LEARNING_MICROFRONTEND_ALIASES", []
    )
    if LEARNING_MICROFRONTEND_ALIASES:
        LEARNING_MICROFRONTEND_ALIASES = json.loads(LEARNING_MICROFRONTEND_ALIASES)

    if settings.LEARNING_MICROFRONTEND_URL not in LEARNING_MICROFRONTEND_ALIASES:
        LEARNING_MICROFRONTEND_ALIASES.append(settings.LEARNING_MICROFRONTEND_URL)

    default_alias = "learning.{}.localhost".format(DEREX_PROJECT)
    if default_alias not in LEARNING_MICROFRONTEND_ALIASES:
        LEARNING_MICROFRONTEND_ALIASES.append(default_alias)

    try:
        settings.CORS_ORIGIN_WHITELIST.extend(LEARNING_MICROFRONTEND_ALIASES)
        settings.LOGIN_REDIRECT_WHITELIST.extend(LEARNING_MICROFRONTEND_ALIASES)
    except AttributeError:
        # This is the lms.envs.common settings loading the plugins
        # We simply pass here since plugins will be properly loaded
        # by derex django default settings
        pass
