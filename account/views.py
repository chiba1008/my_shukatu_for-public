import email
import imp
from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError


def signup_func(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.create_user(username,email,password)
            return render(request, 'shukatu/index.html', {})
        except IntegrityError:
            return render(request, 'account/signup.html', {'error':'このユーザーネームはすでに登録されています。'})

    return render(request, 'account/signup.html', {})

def login_func(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('shukatu:home')
        
        else:
            return render(request, 'account/login.html', {'context':'not logged in'})
    return render(request, 'account/login.html', {'context':'get method'})

def logout_func(request):
    logout(request)
    return redirect('shukatu:index')