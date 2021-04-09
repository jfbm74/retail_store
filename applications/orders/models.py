from django.db import models
from datetime import datetime

# models
from applications.users.models import User
from applications.products.models import Product


# Create your models here.
class Order(models.Model):
    """Define Order Model in Database"""
    date = models.DateTimeField('order date', auto_created=True, null=True)
    subtotal = models.FloatField('subtotal', null=True)
    taxes = models.FloatField('tax import', null=True)
    paid = models.BooleanField('is_paid', default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    class Meta:
        """ Meta class"""
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ['-id']

    def __str__(self):
        """ String Representation class"""
        return str(self.id)
