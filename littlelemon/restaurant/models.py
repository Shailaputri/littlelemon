from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.
class BookingTable(models.Model):
	name = models.CharField(max_length = 255, null=True, blank=True)
	no_of_guests = models.IntegerField(null=True, blank=True)
	bookingdate = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class Menu(models.Model):
	title = models.CharField(max_length =255, null=True, blank=True)
	price = models.DecimalField(max_digits = 10, decimal_places = 2, null=True, blank=True)
	inventory = models.IntegerField(null=True, blank=True)




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