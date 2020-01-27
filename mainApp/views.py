from django.shortcuts import render
from mainApp.models import Services


def index(request):
    services = Services.objects.all()
    return render(request, 'mainApp/homePage.html', {"services": services})
	
def view_favicon(request):
    return render(request, 'mainApp/favicon.ico')