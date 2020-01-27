from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
	path('favicon.ico/', views.view_favicon, name='view_favicon'),
]
