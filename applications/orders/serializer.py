from rest_framework import  serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    """Serialize Product objects to JSON"""
    class Meta:
        """Class Meta"""
        model = Order
        fields = '__all__'
