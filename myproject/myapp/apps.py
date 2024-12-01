from django.apps import AppConfig
from django.core.management import call_command

class MyAppConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        # Викликаємо міграції при старті додатку
        call_command('makemigrations')
        call_command('migrate')
        
