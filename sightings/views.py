from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.db.models import Count


from map.models import Squirrel
from .forms import SquirrelForm

def all_squirrels(request):
    squirrels = Squirrel.objects.all()
    paginator = Paginator(squirrels, 36) # show 30 squirrels per page

    page = request.GET.get('page')
    squirrels = paginator.get_page(page)
    context = {
        'squirrels': squirrels,
    }
    return render(request, 'sightings/all.html', context)


def edit_squirrel(request, squirrel_id):
    squirrel = Squirrel.objects.get(unique_squirrel_id=squirrel_id)
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
            x=form['unique_squirrel_id'].value()
            form.save()
            return redirect(f'/sightings/{x}/')
    else:
        form = SquirrelForm()

    context = {
        'form': form,
    }

    return render(request, 'sightings/add.html', context)


def stats(request):
    total_squarrel = Squirrel.objects.count()
    color_lst = Squirrel.objects.values('primary_fur_color').annotate(c=Count('primary_fur_color'))
    age_lst = Squirrel.objects.values('age').annotate(c=Count('age'))
    shift_lst = Squirrel.objects.values('shift').annotate(c=Count('shift'))
    location_lst = Squirrel.objects.values('location').annotate(c=Count('location'))

    context = {
        'total_squarrel':total_squarrel,
        'color_lst':color_lst,
        'age_lst':age_lst,
        'shift_lst':shift_lst,
        'location_lst':location_lst,
    }

    return render(request, 'sightings/stats.html', context)
