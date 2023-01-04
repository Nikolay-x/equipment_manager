import logging
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, login

from em_asd.accounts.forms import UserCreateForm
from em_asd.pumps.models import Pump
from em_asd.accounts.tasks import time_consuming_operation

# Create your views here.


UserModel = get_user_model()


class UserDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    template_name = 'accounts/profile_details.html'
    model = UserModel


@login_required
def favourites_list(request):
    pumps = Pump.objects.filter(favourites=request.user)

    context = {
        'pumps': pumps,
    }

    return render(request, 'accounts/favourites.html', context)


@login_required
def add_remove_favourites(request, pump_id):
    pump = get_object_or_404(Pump, id=pump_id)
    if pump.favourites.filter(id=request.user.id).exists():
        pump.favourites.remove(request.user)
    else:
        pump.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


# class SignUpView(views.CreateView):
#     template_name = 'accounts/profile_sign_up.html'
#     form_class = UserCreateForm
#     success_url = reverse_lazy('home page')
#
#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)
#         if self.object:
#             login(request, self.object)
#         return response


class SignUpView(views.CreateView):
    template_name = 'accounts/profile_sign_up.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('home page')

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if self.object:

            time_consuming_operation.delay()
            # time_consuming_operation()

            login(request, self.object)
            login_time = datetime.now()
            logging.info(f"User {request.user} was logged in at {login_time}.")
        return response


class SignInView(auth_views.LoginView):
    template_name = 'accounts/profile_sign_in.html'


class SignOutView(auth_mixins.LoginRequiredMixin, auth_views.LogoutView):
    next_page = reverse_lazy('home page')


class UserEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    template_name = 'accounts/profile_edit.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'email', 'photo',)

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={
            'pk': self.request.user.pk,
        })


class UserDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    template_name = 'accounts/profile_delete.html'
    model = UserModel
    success_url = reverse_lazy('home page')
