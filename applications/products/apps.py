from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """ This class is required for django to identify a new application"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.products'
