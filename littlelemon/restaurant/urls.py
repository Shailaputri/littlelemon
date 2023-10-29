from django.urls import path
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
path('', views.home, name='home'),
path('index/', views.index, name='index'),
path('menu/', views.MenuView.as_view(), name='menu'),
path('menu/<int:pk>', views.SingleMenuView.as_view(), name='single_menu'),
path('register/', views.RegisterView.as_view()),
path('api-token-auth/', obtain_auth_token),
path('menu_items', views.menu_items, name='menu_items'),
path('book/', views.book, name="book"),
path('bookings/', views.bookings, name="bookings"),
path('allbookings/', views.allbookings, name="allbookings"),
# path('msg/',views.msg, name='msg'),
]
