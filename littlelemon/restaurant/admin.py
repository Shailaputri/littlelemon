from django.contrib import admin
from . import models

'''
Imported both Book and Menu models
for use in admin site.
'''
models_list = (models.BookingTable, models.Menu, models.Category)
for m in models_list:
   admin.site.register(m)

