from django.apps import AppConfig


class BrewConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'brew'
    
    def ready(self):
        import brew.schema
