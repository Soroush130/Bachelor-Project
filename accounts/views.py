from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import LoginUserForm, RegisterUserForm


def log_in(request):
    url = request.META.get("HTTP_REFERER")
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        login_form = LoginUserForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Success Login')
                return redirect('/')
            else:
                return redirect(url)
    else:
        login_form = LoginUserForm()

    context = {
        'login_form': login_form,
    }
    return render(request, 'accounts/login.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        register_form = RegisterUserForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data["username"]
            email = register_form.cleaned_data["email"]
            password = register_form.cleaned_data["password"]
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Success Register')
            return redirect('/accounts/login')
    else:
        register_form = RegisterUserForm()

    context = {
        'register_form': register_form,
    }
    return render(request, 'accounts/register.html', context)


def log_out(request):
    logout(request)
    return redirect('/accounts/login')
