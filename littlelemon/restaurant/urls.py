from django.urls import path
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
path('home/', views.home, name='home'),
# path('', views.index, name='index'),
path('menu/', views.MenuView.as_view(), name='menu'),
path('menu/<int:pk>', views.SingleMenuView.as_view(), name='single_menu'),
path('msg/',views.msg, name='msg'),
path('api-token-auth/', obtain_auth_token),
]