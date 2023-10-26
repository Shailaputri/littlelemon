from django.test import TestCase
from restaurant import models

class MenuTest(TestCase):
	'''
	Test module tests creation of Menu model of restaurant app
	'''
	def create_menu(self):
		return models.Menu.objects.create(title="IceCream", price=80, inventory=100)
	def test_menu_creation(self):
		menu = self.create_menu()
		self.assertTrue(isinstance(menu, models.Menu))
		self.assertEqual(menu.get_menu(), "IceCream : 80")

class BookingTableTest(TestCase):
	'''
	Test module tests creation of Booking Table model of restaurant app
	'''
	def create_booking_table(self):
		return models.BookingTable.objects.create(name="Adam", no_of_guests = 2)

	def test_booking_table_creation(self):
		book = self.create_booking_table()
		self.assertTrue(isinstance(book, models.BookingTable))
		self.assertEqual(book.get_booking(), "Adam : 2")
