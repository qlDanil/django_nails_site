from django.urls import path
from . import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', views.index, name='index'),
	path('favicon.ico', RedirectView.as_view(url='/static/mainApp/icons/favicon.ico'), name='favicon'),
]
