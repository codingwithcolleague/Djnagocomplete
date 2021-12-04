from django.apps import AppConfig


class SignaltaskConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signaltask'

    def ready(self):
        import signaltask.signal