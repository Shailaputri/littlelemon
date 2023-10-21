from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics
from . import models, serializers

# Create your views here.
def home(request):
	return HttpResponse('Hello')

def index(request):
	return render(request, 'index.html', {})

class MenuView(generics.ListCreateAPIView):
	'''
	handles the POST and GET method calls.
	'''
	queryset = models.Menu.objects.all()
	serializer_class = serializers.MenuSerializer

class SingleMenuView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
	'''
	GET, PUT and DELETE method calls.
	'''
	queryset = models.Menu.objects.all()
	serializer_class = serializers.MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
	queryset = models.BookingTable.objects.all()
	serializer_class = serializers.BookingTableSerializer