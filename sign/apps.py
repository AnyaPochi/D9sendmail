from django.apps import AppConfig


class SignConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sign'

class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'
    def ready(self):
        import news.signals
