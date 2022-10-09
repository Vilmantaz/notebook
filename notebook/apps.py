from django.apps import AppConfig


class NotebookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notebook'

    def ready(self):
        from .signals import create_profile, save_profile
