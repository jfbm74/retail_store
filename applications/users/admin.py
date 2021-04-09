from django.contrib import admin
from .models import (
    User,
)

# Register your models here.


# Presentation in django admin panel
class UserAdmin(admin.ModelAdmin):
    """ Presentation in django admin panel """
    list_display = (
        'id',
        'name',
        'last_name',
        'gov_id',
        'email',
        'company',
    )
    search_fields = ('email', 'name', 'last_name')


admin.site.register(User, UserAdmin)
