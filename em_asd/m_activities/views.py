from django.contrib.auth.decorators import login_required
from django.contrib.auth import mixins as auth_mixins
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views

from em_asd.core.decorators import allow_groups
from em_asd.m_activities.forms import ActivityAddForm
from em_asd.m_activities.models import Activity
from em_asd.pumps.models import Pump


# Create your views here.


@login_required
def activities_list(request):
    search_item = request.GET.get('pattern', None)

    if search_item:
        open_activities = Activity.objects.filter(status='Open')
        open_activities = open_activities.filter(Q(description__icontains=search_item))

        close_activities = Activity.objects.filter(status='Close')
        close_activities = close_activities.filter(Q(description__icontains=search_item))
    else:
        open_activities = Activity.objects.filter(status='Open')
        close_activities = Activity.objects.filter(status='Close')

    context = {
        'open_activities': open_activities,
        'close_activities': close_activities,
    }

    return render(request, 'm_activities/activities.html', context)


@login_required
@allow_groups(groups=['Engineer'])
def activity_add(request, pump_id):
    pump = Pump.objects.filter(pk=pump_id) \
        .get()

    if request.method == 'GET':
        form = ActivityAddForm()
    else:
        form = ActivityAddForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.pump = pump
            form.save()
            return redirect('pumps list')

    context = {
        'form': form,
        'pump_id': pump_id,
    }

    return render(request, 'm_activities/activity_add.html', context)


@method_decorator(allow_groups(groups=['Engineer']), name='dispatch')
class ActivityEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Activity
    fields = ('description', 'due_date', 'status',)
    template_name = 'm_activities/activity_edit.html'
    success_url = reverse_lazy('activities')


@method_decorator(allow_groups(groups=['Engineer']), name='dispatch')
class ActivityDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = Activity
    template_name = 'm_activities/activity_delete.html'
    fields = ('description', 'due_date', 'status',)
    success_url = reverse_lazy('activities')
