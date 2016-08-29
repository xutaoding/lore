from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from . import forms


# Create your views here.
def user_login(request):
    template_name = 'login.html'

    if request.method == 'GET':
        return render(request, template_name, {})

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/index/')
            else:
                pass
        else:
            return HttpResponseRedirect(reverse('accounts:login'))


def user_register(request):
    template_name = 'register.html'

    if request.method == 'GET':
        return render(request, template_name)

    if request.method == 'POST':
        register_form = forms.UserForm(request.POST)

        if request.POST.get('password', '') != request.POST.get('password_again'):
            return HttpResponse(content={'status': 404, 'message': 'password error.'})

        if register_form.is_valid():
            register_form.save()
    return HttpResponseRedirect(reverse('accounts:login'))



