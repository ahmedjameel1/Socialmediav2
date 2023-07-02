from django.apps import AppConfig


class AppImagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_images'

    def ready(self):
        # import signal handlers
        import app_images.signals
