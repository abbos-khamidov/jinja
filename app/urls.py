
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('contacts', views.contacts),
    path('about', views.about),
]
