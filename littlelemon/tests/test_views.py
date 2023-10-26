from django.test import TestCase
from django.test.client import Client
from rest_framework.test import APIClient
# from django.contrib.auth import User
from restaurant import models
from rest_framework import authtoken

from django.contrib.auth.models import User
from restaurant import views, models
from setuptools import setup
from django.urls import reverse

class GetMenuViewTest(TestCase):
	'''
	Test module tests Menu API
	'''
	def set_up(self):
		self.falafel = models.Menu.objects.create(title="Falafel", price=12, inventory=5),
		self.burger = models.Menu.objects.create(title="Burger", price=5, inventory=25),
		self.burrito = models.Menu.objects.create(title="Burrito", price=50, inventory=5),
	

	def test_get_menu_view(self):
		self.set_up()
		self.user = User.objects.create_user(username="testuser", password="mnbvcxza!")
		self.client = APIClient()
		self.client.force_authenticate(user=self.user)
		response = self.client.get('/restaurant/menu/menu/')
		self.assertEqual(response.status_code, 200)

class GetBookingTableiewTest(TestCase):
	'''
	Test module to tests Booking Table API
	'''

	def set_up(self):
		self.adam = models.BookingTable.objects.create(name="Adam", no_of_guests = 2)
	
	def test_get_booking_table_view(self):
		self.set_up()
		self.user = User.objects.create_user(username="testuser", password="mnbvcxza!")
		self.client = APIClient()
		self.client.force_authenticate(user=self.user)
		response = self.client.get('/restaurant/booking/tables/')
		self.assertEqual(response.status_code, 200)








