from django.urls import path
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token


#front-end urls
urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('simple_menu/', views.simple_menu, name='simple_menu'),
path('single_menu_item/<int:pk>/', views.display_menu_items, name='single_menu_item'),
path('book/', views.book, name="book"),
path('bookings/', views.bookings, name="bookings"),
path('allbookings/', views.allbookings, name="allbookings"),
# path('msg/',views.msg, name='msg'),
]

#forms to update menu
urlpatterns += [
path('menu_items/', views.menu_items, name='menu_items'),
]

#api endpoints
urlpatterns += [
path('menu/', views.MenuView.as_view(), name='menu'),
path('menu/<int:pk>', views.SingleMenuView.as_view(), name='single_menu'),
path('register/', views.RegisterView.as_view()),
path('api-token-auth/', obtain_auth_token),
path('category/', views.CategoriesView.as_view(), name='category'),
path('ratings/', views.RatingsView.as_view(), name='ratings'),
path('cart/', views.CartView.as_view(), name='cart'),
path('order/', views.OrderView.as_view(), name='order'),
path('orderitem/', views.OrderItemView.as_view(), name='order_item'),
path('groups/manager/users/', views.manager, name='groups_manager')
]

#Register - register/

#Login - /auth/token/login/


#view token- api-token-auth/

#assign user to manager group - groups/manager/users/
