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
    """Test Caases for User Class."""

    def test_upper(self):
        """ Check if is upper"""
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        """ Check if is upper and lower"""
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        """ Check a string"""
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
