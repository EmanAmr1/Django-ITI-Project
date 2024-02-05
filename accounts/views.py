from django.shortcuts import render, redirect, reverse
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.

''''
def mylogin(request):
    context = {'form': autenticate()}
    return render(request, 'registration/login')
'''


def mylogout(request):

    return render(request, 'registration/logout')


def myprofile(request):

    return redirect(reverse('product_list'))


class RegisterForm(CreateView):
    model = User
    template_name = 'registration/resgister.html'
    form_class = UserCreationForm
    context_object_name = 'form'
    success_url=reverse_lazy('login')
