from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        """Class Meta"""
        model = User
        fields = [
            'email',
            'name',
            'last_name',
            'gov_id',
            'company',
        ]
