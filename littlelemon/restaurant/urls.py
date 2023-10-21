from django.urls import path
from . import views

urlpatterns = [
path('home/', views.home, name='home'),
path('', views.index, name='index'),
path('menu/', views.MenuView.as_view(), name='menu'),
path('menu/<int:pk>', views.SingleMenuView.as_view(), name='single_menu'),
]