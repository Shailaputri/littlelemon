from django.tests import TestCase
from restaurant import models

class MenuTest(TestCase):
	def create_menu(self):
		return models.Menu.objects.create(title="IceCream", price=80, inventory=100)
	def test_menu_creation(self):
		menu = self.create_menu()
		self.assertTrue(isinstance(menu, models.Menu))
		self.assertEqual(item, "IceCream : 80")

# class MenuTest(TestCase):
# def test_get_item(self):
# 	item = models.Menu.objects.create(title="IceCream", price=80, inventory=100)
# 	self.assertEqual(item, "IceCream : 80")
