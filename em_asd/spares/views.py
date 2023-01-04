from django.contrib.auth.decorators import login_required
from django.contrib.auth import mixins as auth_mixins
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views

from em_asd.core.decorators import allow_groups
from em_asd.pumps.models import Pump
from em_asd.spares.forms import SparesAddForm
from em_asd.spares.models import Spares


# Create your views here.


@login_required
def spares_list(request):
    search_item = request.GET.get('pattern', None)

    if search_item:
        spares = Spares.objects.filter(Q(ref_doc_code__icontains=search_item))
    else:
        spares = Spares.objects.all()

    context = {
        'spares': spares,
    }

    return render(request, 'spares/spares.html', context)


@login_required
@allow_groups(groups=['Engineer'])
def spares_add(request, pump_id):
    pump = Pump.objects.filter(pk=pump_id) \
        .get()

    if request.method == 'GET':
        form = SparesAddForm()
    else:
        form = SparesAddForm(request.POST)
        if form.is_valid():
            spares = form.save(commit=False)
            spares.pump = pump
            form.save()
            return redirect('pumps list')

    context = {
        'form': form,
        'pump_id': pump_id,
    }
    return render(request, 'spares/spares_add.html', context)


@method_decorator(allow_groups(groups=['Engineer']), name='dispatch')
class SparesEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Spares
    fields = ('name', 'ref_doc_code', 'location', 'quantity',)
    template_name = 'spares/spares_edit.html'
    success_url = reverse_lazy('spares')


@method_decorator(allow_groups(groups=['Engineer']), name='dispatch')
class SparesDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = Spares
    template_name = 'spares/spares_delete.html'
    success_url = reverse_lazy('spares')
