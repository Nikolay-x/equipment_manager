from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from em_asd.core.decorators import allow_groups
from em_asd.core.utils import check_if_engineer
from em_asd.manuals.forms import ManualAddForm, ManualDeleteForm
from em_asd.manuals.models import Manual
from em_asd.pumps.models import Pump


# Create your views here.


@login_required
def manuals_list(request):
    search_item = request.GET.get('pattern', None)

    if search_item:
        manuals = Manual.objects.filter(Q(name__icontains=search_item))
    else:
        manuals = Manual.objects.all()

    engineer = check_if_engineer(request)

    context = {
        'manuals': manuals,
        'engineer': engineer,
    }

    return render(request, 'manuals/manuals.html', context)


@login_required
@allow_groups(groups=['Engineer'])
def manual_add(request, pump_id):
    pump = Pump.objects.filter(pk=pump_id) \
        .get()

    if request.method == 'GET':
        form = ManualAddForm()
    else:
        form = ManualAddForm(request.POST)
        if form.is_valid():
            manual = form.save(commit=False)
            manual.pump = pump
            form.save()
            return redirect('pumps list')

    context = {
        'form': form,
        'pump_id': pump_id,
    }
    return render(request, 'manuals/manual_add.html', context)


@login_required
@allow_groups(groups=['Engineer'])
def manual_delete(request, manual_id):
    manual = Manual.objects.filter(pk=manual_id).get()

    if request.method == 'GET':
        form = ManualDeleteForm(instance=manual)
    else:
        form = ManualDeleteForm(request.POST, instance=manual)
        manual.delete()
        return redirect('manuals')

    context = {
        'form': form,
        'manual': manual,
        'manual_id': manual_id,
    }

    return render(request, 'manuals/manual_delete.html', context)
