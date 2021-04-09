from rest_framework import viewsets

from .models import Product
from .serializer import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """ Returns Objects from database"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
