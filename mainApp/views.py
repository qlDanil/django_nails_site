from django.shortcuts import render
from mainApp.models import Services


def index(request):
    services = Services.objects.all()
    return render(request, 'mainApp/homePage.html', {"services": services})


def contact(request):
    return render(request, 'mainApp/basic.html',
                  {'values': ['Если у вас остались вопросы, то задавайте их мне по телефону', '+7 (913) 185-98-76']})
