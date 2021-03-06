from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Managers
from .managers import UserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    """Define User Model in Database"""
    email = models.EmailField('email', unique=True)
    name = models.CharField('first name', max_length=50, blank=True)
    last_name = models.CharField('last name', max_length=50, blank=True)
    gov_id = models.CharField('legal id', unique=True, max_length=10)
    company = models.CharField('company name', max_length=100, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        """ Meta class"""
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ['-id']

    def __str__(self):
        """ String Representation class"""
        return self.email
