from django.contrib import admin
from django.urls import path
from . import views

app_name = 'aliens'

urlpatterns = [
    path('', views.home , name='home'),
    path('register', views.register, name='register'),
    path('list/', views.aliens_list, name='alien_list'),
    path('counter/', views.alien_counter, name='alien_counter'),
]
