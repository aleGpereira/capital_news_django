from django.apps import AppConfig


class ReporterConfig(AppConfig):
    name = 'reporter'

    def ready(self):
        import reporter.signals
