from rest_framework import viewsets

from .models import Order
from .serializer import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """ Returns Objects from database"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

