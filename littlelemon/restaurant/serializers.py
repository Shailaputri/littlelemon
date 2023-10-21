from rest_framework import serializers
from restaurant.models import Menu, BookingTable

class MenuSerializer(serializers.ModelSerializer):
	class Meta:
		model = Menu
		fields = '__all__'

class BookingTableSerializer(serializers.ModelSerializer):
	class Meta:
		model = BookingTable
		fields = '__all__'


