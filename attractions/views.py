from django.shortcuts import render
from django.http import HttpResponse

from .models import City


def index(request):
    return HttpResponse("Hello from attractions app")


def cities(request):
    context = {
        'cities': City.objects.all()
    }
    return render(request, 'city/index.html', context)


def city(request, **kwargs):
    city_id = kwargs['city_id']
    result = City.objects.filter(id=city_id)
    return HttpResponse(f"Hello from attractions app {result[0].name}")


def attraction(request, **kwargs):
    city_id = kwargs['city_id']
    attraction_id = kwargs['attraction_id']
    return HttpResponse(f"Hello from attractions app {city_id} {attraction_id}")
