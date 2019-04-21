from django.contrib import admin
from django.urls import path
from . import views

app_name = 'aliens'

urlpatterns = [
    path('', views.home , name='home'),
]
