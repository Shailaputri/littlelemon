from django.shortcuts import render, get_object_or_404
from django.core import serializers as core_serializer
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, generics
from . import models, serializers, forms
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.contrib.auth.models import User
from datetime import datetime
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User,Group
from rest_framework import status





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
	menu_data = models.Menu.objects.all().order_by('title')
	main_data = {"menu" : menu_data}
	return render(request, "simple_menu.html", main_data)

def display_menu_items(request, pk=None):
	if pk:
		menu_item = models.Menu.objects.get(pk=pk)
	else:
		menu_item = ''
	return render(request, "single_menu_item.html", {"menu_item":menu_item})

#Generics class based views for Menu, Single Menu and Booking - DRF Project
class CategoriesView(generics.ListCreateAPIView):
	queryset = models.Category.objects.all()
	serializer_class = serializers.CategorySerializer

class MenuView(generics.ListCreateAPIView):
	'''
	handles the POST and GET method calls of Menu API
	'''
	queryset = models.Menu.objects.all()
	serializer_class = serializers.MenuSerializer
	ordering_fields = ['price', 'inventory']
	filterset_fields = ['price', 'inventory']
	search_fields = ['title']

class SingleMenuView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
	'''
	GET, PUT and DELETE method calls of Booking Table API
	'''
	
	queryset = models.Menu.objects.all()
	serializer_class = serializers.MenuSerializer
	
class RatingsView(generics.ListCreateAPIView):
	throttle_classes = [AnonRateThrottle, UserRateThrottle]
	queryset = models.Rating.objects.all()
	serializer_class = serializers.RatingSerializer
	def get_permissions(self):
		if self.request.method == 'GET':
			return []
		return [IsAuthenticated()]


class BookingViewSet(viewsets.ModelViewSet):
	'''
	Creating view for booking tables and securing it
	'''
	permission_classes=[IsAuthenticated]
	queryset = models.BookingTable.objects.all()
	serializer_class = serializers.BookingTableSerializer

class CartView(generics.ListCreateAPIView):
	queryset = models.Cart.objects.all()
	serializer_class = serializers.CartSerializer
	def get_permissions(self):
		if not self.request.user.groups.filter(name = 'Customer').exists():
			return []
		return [IsAuthenticated()]


class OrderView(generics.ListCreateAPIView):
	queryset = models.Order.objects.all()
	serializer_class = serializers.OrderSerializer

class OrderItemView(generics.ListCreateAPIView):
	queryset = models.OrderItem.objects.all()
	serializer_class = serializers.OrderItemSerializer


#function based views to implement Menu and Reservation booking forms
def menu_items(request):
	form = forms.MenuForm()
	if request.method == 'POST':
		form = forms.MenuForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			mf = models.Menu(title = cd['title'], price = cd['price'], inventory = cd['inventory'], description = cd['description'], category = cd['category'])
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

@api_view(['POST'])
@permission_classes([IsAdminUser])
def manager(request):
	username = request.data['username']
	if username:
		user = get_object_or_404(User, username=username)
		manager = Group.objects.get(name = 'Manager')
		if request.method == 'POST':
			manager.user_set.add(user)
		elif request.method == 'DELETE':
			manager.user_set.remove(user)
		return HttpResponse("{'message': 'user added to the manager group'}", content_type = 'application/json')
	return HttpResponse("{'message':'error'}", status.HTTP_400_BAD_REQUEST, content_type = 'application/json')

	






# @api_view()
# @permission_classes([IsAuthenticated])
# def msg(request):
# 	return HttpResponse({'message: View is protected.'})
