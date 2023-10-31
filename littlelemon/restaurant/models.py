from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from datetime import datetime
from django.utils import timezone


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
	# class Meta :
	# 	verbose_name_plural = "Categories"
	# slug = models.SlugField(null=True, blank=True)
	slug = models.SlugField()
	title = models.CharField(max_length = 255)
	# slug = models.AutoSlugField(populate_from='title', unique=True)
	
	

	def __str__(self):
		return self.title

class Menu(models.Model):
	'''
	Menu model defines attributes of food menu
	in LittleLemon restaurant.
	'''
	category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
	title = models.CharField(max_length =255, null=True, blank=True)
	price = models.DecimalField(max_digits = 10, decimal_places = 2, null=True, blank=True)
	inventory = models.IntegerField(null=True, blank=True)
	description = models.TextField(null=True, blank=True, max_length=1000, default='')
	

	def __str__(self):
		return f'{self.title} : {str(self.price)} is added.'
	def get_menu(self):
		return f'{self.title} : {str(self.price)}'








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