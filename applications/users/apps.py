from django.apps import AppConfig


class UsersConfig(AppConfig):
    """ This class is required for django to identify a new application"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.users'
