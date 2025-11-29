from django.contrib import admin
from django.urls import path
from testCart import views

app_name = 'testCart'

urlpatterns = [
    path('add/', views.addCart, name='addCart'),
    path('change/', views.changeCart, name='changeCart'),
    path('remove/', views.removeCart, name='removeCart'),
]