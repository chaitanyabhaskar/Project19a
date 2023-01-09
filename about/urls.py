from django.contrib import admin
from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('',views.about,name='about')
]