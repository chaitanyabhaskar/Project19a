
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('results',include('res.urls')),
    path("",include('intro.urls')),
    path('admin/', admin.site.urls),
    path("home/",include('home.urls')),
    path('about',include('about.urls')),
    path('accounts/',include('accounts.urls')),
]