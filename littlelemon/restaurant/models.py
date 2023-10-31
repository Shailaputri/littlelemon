from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class BookingTable(models.Model):
	'''
	Booking Table model defines attributes of booking a table 
	in LittleLemon restaurant.
	'''
	name = models.CharField(max_length = 255, null=True, blank=True)
	no_of_guests = models.IntegerField(null=True, blank=True)
	bookingdate = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	reservation_slot = models.SmallIntegerField(default = 10)
	reservation_date = models.DateTimeField(default=timezone.now())

	def __str__(self):
		return f'Your booking confirmed under {self.name} for {self.no_of_guests} \
		on {self.bookingdate}.'
	def get_booking(self):
		return f'{self.name} : {str(self.no_of_guests)}'

class Category(models.Model):
	'''
	This will have many-to-one relationship 
	with Menu model. 
	'''
	class Meta :
		verbose_name_plural = "Categories"
	# slug = models.SlugField(null=True, blank=True)
	slug = models.SlugField()
	title = models.CharField(max_length = 255, db_index=True)
	# slug = models.AutoSlugField(populate_from='title', unique=True)
	
	

	def __str__(self):
		return self.title

class Menu(models.Model):
	'''
	Menu model defines attributes of food menu
	in LittleLemon restaurant.
	Menu : Category = Many : 1
	'''
	category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
	title = models.CharField(max_length =255, null=True, blank=True, db_index = True)
	price = models.DecimalField(max_digits = 10, decimal_places = 2, null=True, blank=True)
	inventory = models.IntegerField(null=True, blank=True)
	description = models.TextField(null=True, blank=True, max_length=1000, default='')
	# featured = models.BooleanField(default= 0, db_index = True)

	def __str__(self):
		return self.title

class Cart(models.Model):
	'''
	Cart : Menu = Many : 1
	1 Menu present in many user carts.
	1 cart will have 1 menu item
	'''
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	menuitem = models.ForeignKey(Menu, on_delete = models.CASCADE)
	quantity = models.SmallIntegerField()
	unit_price = models.DecimalField(max_digits = 10, decimal_places =2)
	price = models.DecimalField(max_digits = 10, decimal_places =2)
	

	def __str__(self):
		return f'No of items in cart : {str(self.quantity)}'

	def get_cart_total(self):
		self.price = self.quantity * self.unit_price
		return self.price

class Order(models.Model):
	'''
	Order created with menu items. On click, menu items move from Cart to Order table
	Many Orders per user per delivery crew.
	'''

	
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	date = models.DateTimeField(default=timezone.now())
	total = models.DecimalField(max_digits = 10, decimal_places = 2)
	status = models.BooleanField(db_index = True, default = 0)
	delivery_crew = models.ForeignKey(User, on_delete = models.SET_NULL, related_name = 'delivery_crew', null=True)
	
	def __str__(self):
		return f'Order created on {str(self.date)} : Delivery Status: {str(self.status)} : Total:{str(self.total)}'


class OrderItem(models.Model):
	'''
	Many order items per order
	and Order ID is created.
	'''
	order = models.ForeignKey(User, on_delete = models.CASCADE)
	menuitem = models.ForeignKey(Menu, on_delete = models.CASCADE)
	quantity = models.SmallIntegerField()
	unit_price = models.DecimalField(max_digits = 10, decimal_places =2)
	price = models.DecimalField(max_digits = 10, decimal_places =2)

	def __str__(self):
		return f'No of items in cart : {str(self.quantity)}'

	def get_order_total(self):
		self.price = self.quantity * self.unit_price
		return self.price
	



class Rating(models.Model):
	'''
	Rating model defines attributes of rating
	model
	'''
	menuitem_id = models.SmallIntegerField()
	rating = models.SmallIntegerField()
	user = models.ForeignKey(User, on_delete = models.CASCADE)







'''
For validations:
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )
'''