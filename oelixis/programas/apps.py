from django.apps import AppConfig


class ProdutoConfig(AppConfig):
    name = 'programas'
    def ready(self):
        import programas.signals

class PollsConfig(AppConfig):
    name = 'programas'
