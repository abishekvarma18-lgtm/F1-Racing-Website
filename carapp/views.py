from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login,logout      
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')

def second(request):
    return render(request, 'second.html')

def drive(request):
    return render(request, 'drive.html')

def team(request):
    return render(request, 'team.html')

def membership(request):
    return render(request, 'membership.html')

def subscribe(request):
    return render(request, 'subscribe.html')

def payment(request): 
    return render(request, 'payment.html')  

def login_view(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('index')

        return render(request, 'login.html', {
            'error': 'Invalid username or password'
        })

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def register_view(request):
    if request.method == "POST":

        fullname = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')

        if password != confirm_password:
            return render(request, 'register.html', {
                'error': 'Passwords do not match'
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {
                'error': 'Username already exists'
            })

        User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=fullname
        )

        return redirect('login')

    return render(request, 'register.html') 