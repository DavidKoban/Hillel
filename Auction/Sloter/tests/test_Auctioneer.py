import pytest
from django.test import TestCase
from App_1.models import Auctioneer
import unittest


class test_Auctioneer(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Auctioneer.objects.create(name='Big',
                                  surname='Bob',
                                  patronymic="Pob",
                                  password="1234",
                                  email="example@gmail.com",
                                  birthday='2001-01-01'
                                  )

    def test_name(self):
        auctioneer = Auctioneer.objects.first()
        field_label = auctioneer.name
        self.assertEqual(field_label, 'Big')
