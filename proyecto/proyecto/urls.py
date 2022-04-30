# miPrimerApp/urls.py

from django.contrib import admin
from django.urls import path
from proyectoApp import views
from django.conf import settings

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.index, name='index'),
]