from django.shortcuts import render
from mainApp.models import Services
from django.contrib.staticfiles.views import serve


def index(request):
    services = Services.objects.all()
    return render(request, 'mainApp/homePage.html', {"services": services})
	
def view_favicon(request):
    return serve(request, 'mainApp/favicon.ico')