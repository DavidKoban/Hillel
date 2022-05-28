import pytest
from django.test import TestCase
from Sloter.models import User
import unittest


class test_User(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create(name='Big',
                                  surname='Bob',
                                  patronymic="Pob",
                                  password="1234",
                                  email="example@gmail.com",
                                  birthday='2001-01-01'
                                  )

    def test_name(self):
        auctioneer = User.objects.first()
        field_label = auctioneer.name
        self.assertEqual(field_label, 'Big')
