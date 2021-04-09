from rest_framework import viewsets

from .models import User
from .serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """ Returns Objects from database"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
