from django.apps import AppConfig


class ResourceConfig(AppConfig):
    name = 'service.backends.resource'
    verbose_name = '发票数据'

    def ready(self):
        try:
            from .signals import handlers
        except ImportError as e:
            raise e