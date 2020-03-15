from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules


class NavigationConfig(AppConfig):
    name = "navigation"

    def ready(self):
        autodiscover_modules("navigation")
