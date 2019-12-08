from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrel

# Create your views here.


def index(request):
    context = {"sightings": Squirrel.objects.all()[:50]}
    return render(request, 'map/map.html', context)
