import pytest
from django.test import TestCase
from Hillel.Auction.App_1.models import Auctioneer


class test_Auctioneer(TestCase):
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
        field_label = auctioneer._meta.get_field('name').verbose_name
        assert field_label == 'Big', 'Error name'
