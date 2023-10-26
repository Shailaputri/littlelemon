from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics
from . import models, serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.

def home(request):
	return render(request, 'index.html', {})

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



# @api_view()
# @permission_classes([IsAuthenticated])
# def msg(request):
# 	return HttpResponse({'message: View is protected.'})
