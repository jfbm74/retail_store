from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager, models.Manager):
    """ Handles User Auth Process"""
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        """" Form Valid """
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, **extra_fields ):
        """ Creates a normal user"""
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """ Creates a super user"""
        return self._create_user(email, password, True, True, **extra_fields)