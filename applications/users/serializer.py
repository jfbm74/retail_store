from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Serialize User object to Json"""
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
