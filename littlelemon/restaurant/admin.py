from django.contrib import admin
from . import models

# Register your models here.
models_list = (models.BookingTable, models.Menu)
for m in models_list:
   admin.site.register(m)

