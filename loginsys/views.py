
# -*- coding: utf-8 -*-

from django.template.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def signin(request):
    args = {}
    args.update(csrf(request))
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/home/')
        else:
            args['login_error'] = "Неверный логин или пароль!"
            return render_to_response('landing.html', args)
    else:
        args['login_error'] = "Неверный логин или пароль!"
        return render_to_response('landing.html', args)


def signout(request):
    logout(request)
    return redirect('/')


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = authenticate(username=newuser_form.cleaned_data["username"], password=newuser_form.cleaned_data["password2"])
            login(request, newuser)
            return redirect('/home/')
        else:
            args['form'] = newuser_form
    return render_to_response('landing.html', args)