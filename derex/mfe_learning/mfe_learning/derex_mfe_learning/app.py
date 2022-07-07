from django.apps import AppConfig
from openedx.core.djangoapps.plugins.constants import (
    PluginSettings,
    ProjectType,
    SettingsType,
)


class DerexMfeLearningAppConfig(AppConfig):
    name = "derex_mfe_learning"

    plugin_app = {
        PluginSettings.CONFIG: {
            ProjectType.LMS: {
                SettingsType.COMMON: {PluginSettings.RELATIVE_PATH: "settings"},
            },
            ProjectType.CMS: {
                SettingsType.COMMON: {PluginSettings.RELATIVE_PATH: "settings"},
            },
        },
    }
