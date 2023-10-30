from django.shortcuts import render
from django.core import serializers as core_serializer
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, generics
from . import models, serializers, forms
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from datetime import datetime

import json
from django.views.decorators.csrf import csrf_exempt




# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = serializers.RegisterSerializer


#function based views for about, home and menu pages - DJANGO project. 
def about(request):
	return render(request, 'about.html', {})

def home(request):
	return render(request, 'home.html', {})

def simple_menu(request):
	menu_data = models.Menu.objects.all()
	main_data = {"menu" : menu_data}
	return render(request, "simple_menu.html", main_data)

#Generics class based views for Menu, Single Menu and Booking - DRF Project
class MenuView(generics.ListCreateAPIView):
	'''
	handles the POST and GET method calls of Menu API
	'''
	queryset = models.Menu.objects.all()
	serializer_class = serializers.MenuSerializer

class SingleMenuView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
	'''
	GET, PUT and DELETE method calls of Booking Table API
	'''
	
	queryset = models.Menu.objects.all()
	serializer_class = serializers.MenuSerializer
	


class BookingViewSet(viewsets.ModelViewSet):
	'''
	Creating view for booking tables and securing it
	'''
	permission_classes=[IsAuthenticated]
	queryset = models.BookingTable.objects.all()
	serializer_class = serializers.BookingTableSerializer


#function based views to implement Menu and Reservation booking forms
def menu_items(request):
	form = forms.MenuForm()
	if request.method == 'POST':
		form = forms.MenuForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			mf = models.Menu(title = cd['title'], price = cd['price'], inventory = cd['inventory'])
			mf.save()
			return JsonResponse({'message' : 'success'})
	return render(request, 'menu_items.html', {'form': form})

def book(request):
    form = forms.BookingForm()
    if request.method == 'POST':
        form = forms.BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add code for the bookings() view
@csrf_exempt
def bookings(request):
	if request.method == 'POST':
		data = json.load(request)
		exist = models.BookingTable.objects.filter(reservation_date=data['reservation_date']).filter(
            reservation_slot=data['reservation_slot']).exists()
		if exist == False:
			booking = models.BookingTable(name = data['name'], \
				no_of_guests = data['no_of_guests'], reservation_slot = data['reservation_slot'], \
				 reservation_date = data['reservation_date']).save()
			# return render(request, "bookings.html", {'bookings' : booking_json})
		else:
			# return render(request, "bookings.html", {})
			return HttpResponse("{ 'error':1 }", content_type = 'application/json')
	date = request.GET.get('date', datetime.today().date());
	# bookings = models.BookingTable.objects.all()
	bookings = models.BookingTable.objects.all().filter(reservation_date = date);
	booking_json = core_serializer.serialize('json', bookings);
	# return render(request, "bookings.html", {'bookings' : booking_json})
	return HttpResponse(booking_json, content_type = 'application/json')

def allbookings(request):
	date = request.GET.get('date', datetime.today().date());
	bookings = models.BookingTable.objects.all()
	booking_json = core_serializer.serialize('json', bookings);
	return render(request, "bookings.html", {'bookings' : booking_json})
	






# @api_view()
# @permission_classes([IsAuthenticated])
# def msg(request):
# 	return HttpResponse({'message: View is protected.'})
