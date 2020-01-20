from django.urls import path
from django.views.generic import ListView
from works.models import Works


urlpatterns = [
    path('', ListView.as_view(queryset=Works.objects.all().order_by('-id'), template_name="works/works.html")),
]
