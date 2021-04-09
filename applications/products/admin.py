from django.contrib import admin

# models
from .models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    """ Presentation in django admin panel """
    list_display = (
        'id',
        'name',
        'price',
        'tax',
    )


admin.site.register(Product, ProductAdmin)
