from django.contrib import admin

# model
from .models import Order


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    """ Presentation in django admin panel """
    list_display = (
        'id',
        'date',
        'subtotal',
        'taxes',
        'user_id',
    )
    search_fields = ('date', 'user_id')


admin.site.register(Order, OrderAdmin)
