from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from users.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout

def register_view(request):
    if request.method == "GET":
        context = {
            'form' : RegisterForm
        }
        return render(request, 'users/register.html', context = context)

    elif request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect('/users/login/')
        else:
            context ={
                'form' : form
            }

            return render(request, 'users/register.html', context = context)


def login_view(request):
    if request.method == "GET":
        context ={
            'form' : LoginForm
        }
        return render(request, 'users/login.html', context)
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username= username, password = password)
            if user is not None:
                login(request, user)
                return redirect('/product')
            else:
                form.add_error('username', 'Username or password is incorrect!')

        context ={
            'form' : LoginForm
        }

        return render(request, 'users/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('/product')


def profile_view(request):
    if request.method == "GET":
        context = {
            'user' : request.user
        }
        return render(request, 'users/profile.html', context)
