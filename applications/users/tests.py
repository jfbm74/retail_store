# Django
import unittest
from tkinter import Image

from django.test import TestCase

# Python
import tempfile
import json

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status

# Models
from .models import User


class UserTestCase(TestCase):
    def setUp(self):
        """Test case setup."""
        self.user = User.objects.create(
            name='Pablo',
            last_name='Trinidad',
            email='pablotrinidad@fmma.com',
            gov_id='1116555555',
            company='Holberton Cali',
            password='admin123'
        )

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
