from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Serialize Product objects to JSON"""
    class Meta:
        """Class Meta"""
        model = Product
        fields = '__all__'
