from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from map.models import Squirrel
from .forms import SquirrelForm

def all_squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
        'squirrels': squirrels,
    }
    return render(request, 'sightings/all.html', context)

def squirrel_details(request, squirrel_id):
    squirrel = Squirrel.objects.get(UniqueSquirrelID=squirrel_id)
    return HttpResponse(squirrel.UniqueSquirrelID)

def edit_squirrel(request, squirrel_id):
    squirrel = Squirrel.objects.get(UniqueSquirrelID=squirrel_id)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=squirrel)
        # check data with form
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{squirrel_id}')
    else:
        form = SquirrelForm(instance=squirrel)

    context = {
        'form': form,
    }

    return render(request, 'sightings/edit.html', context)

def add_squirrel(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        # check data with form
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/list/')
    else:
        form = SquirrelForm()

    context = {
        'form': form,
        'jazz': True,
    }

    return render(request, 'sightings/edit.html', context)