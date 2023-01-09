
from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('usr1',views.usr1,name='usr1'),
    path('adm',views.adm,name='adm'),
    path('adm2',views.adm2,name='adm2'),
    path('adm3',views.adm3,name='adm3'),
    path('adm4',views.adm4,name='adm4'),
 
    path('adm6',views.adm6,name='adm6'),
]