from django.db import models


# Create your models here.
class Order(models.Model):
    """ Define a product in database"""
    name = models.CharField('product name', max_length=50)
    price = models.IntegerField('unit price')
    tax = models.FloatField('tax')

    class Meta:
        """Meta Class"""
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['name']

    def __str__(self):
        return  self.name
