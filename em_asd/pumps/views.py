import logging
from datetime import datetime
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views

from em_asd.certificates.models import Certificate
from em_asd.core.decorators import allow_groups
from em_asd.core.utils import check_if_engineer
from em_asd.m_activities.models import Activity
from em_asd.manuals.models import Manual
from em_asd.pumps.forms import PumpAddForm, PumpDeleteForm
from em_asd.pumps.models import Pump
from em_asd.spares.models import Spares


# Create your views here.


@login_required
def pumps_list(request):
    search_item = request.GET.get('pattern', None)

    engineer = check_if_engineer(request)

    if search_item:
        pumps = Pump.objects.filter(Q(tag__icontains=search_item))
        pumps_count = pumps.count()
    else:
        pumps = Pump.objects.all()
        pumps_count = Pump.objects.count()

    context = {
        'pumps': pumps,
        'pumps_count': pumps_count,
        'engineer': engineer,
    }

    return render(request, 'pumps/pumps.html', context)


@login_required
def pump_details(request, pump_id):
    pump = Pump.objects.filter(pk=pump_id).get()
    is_favourite = False
    if pump.favourites.filter(id=request.user.id).exists():
        is_favourite = True

    engineer = check_if_engineer(request)

    logging.info(f'Pump {pump.tag} was viewed by {request.user.username}')

    context = {
        'pump': pump,
        'pump_id': pump_id,
        'is_favourite': is_favourite,
        'engineer': engineer
    }

    return render(request, 'pumps/pump_details.html', context)


@login_required
@allow_groups(groups=['Engineer'])
def pump_add(request):
    if request.method == 'GET':
        form = PumpAddForm()
    else:
        form = PumpAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pumps list')

    context = {
        'form': form,
    }

    return render(request, 'pumps/pump_add.html', context)


@method_decorator(allow_groups(groups=['Engineer']), name='dispatch')
class PumpEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Pump
    exclude = ('favourites',)
    fields = ('tag', 'name', 'type', 'model', 'fluid', 'flow_rate', 'head', 'power', 'image_url', )
    template_name = 'pumps/pump_edit.html'

    def get_success_url(self):
        edited_object = self.object
        return reverse_lazy('pump details', kwargs={
            'pump_id': edited_object.pk
        })


@login_required
@allow_groups(groups=['Engineer'])
def pump_delete(request, pump_id):
    pump = Pump.objects.filter(pk=pump_id).get()

    if request.method == 'GET':
        form = PumpDeleteForm(instance=pump)
    else:
        form = PumpDeleteForm(request.POST, instance=pump)
        pump.delete()
        return redirect('pumps list')

    context = {
        'form': form,
        'pump': pump,
        'pump_id': pump_id,
    }

    return render(request, 'pumps/pump_delete.html', context)


@login_required
def pump_activities(request, pump_id):
    pump = Pump.objects.filter(pk=pump_id).get()
    open_activities = Activity.objects.filter(pump=pump, status='Open')
    close_activities = Activity.objects.filter(pump=pump, status='Close')

    context = {
        'open_activities': open_activities,
        'close_activities': close_activities,
        'pump_id': pump_id,
        'pump_tag': pump.tag,
    }

    return render(request, 'pumps/pump_activities.html', context)


@login_required
def pump_certificates(request, pump_id):
    pump = Pump.objects.filter(pk=pump_id).get()
    valid_certificates = Certificate.objects.filter(pump=pump, expiry_date__gt=datetime.today()) | \
                         Certificate.objects.filter(pump=pump, expiry_date__exact=None)
    expired_certificates = Certificate.objects.filter(pump=pump, expiry_date__lte=datetime.today())

    context = {
        'valid_certificates': valid_certificates,
        'expired_certificates': expired_certificates,
        'pump_id': pump_id,
        'pump_tag': pump.tag,
    }

    return render(request, 'pumps/pump_certificates.html', context)


@login_required
def pump_manuals(request, pump_id):
    pump = Pump.objects.filter(pk=pump_id).get()
    manuals = Manual.objects.filter(pump=pump)

    context = {
        'manuals': manuals,
        'pump_id': pump_id,
        'pump_tag': pump.tag,
    }
    return render(request, 'pumps/pump_manuals.html', context)


@login_required
def pump_spares(request, pump_id):
    pump = Pump.objects.filter(pk=pump_id).get()
    spares = Spares.objects.filter(pump=pump)

    context = {
        'spares': spares,
        'pump_id': pump_id,
        'pump_tag': pump.tag,
    }

    return render(request, 'pumps/pump_spares.html', context)
