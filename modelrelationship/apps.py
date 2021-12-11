from django.apps import AppConfig


class ModelrelationshipConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modelrelationship'

    def ready(self):
        import modelrelationship.signals