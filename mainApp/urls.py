from django.urls import path
from . import views
from django.views.generic.base import RedirectView
{% load static %}

urlpatterns = [
    path('', views.index, name='index'),
	path('favicon.iso/', RedirectView.as_view(url="% static 'mainApp/icons/favicon.ico' %}", permanent=True)),
]
