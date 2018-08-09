from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import logging

logger = logging.getLogger('django')

def index(request):
    return render(request, 'twitter/index.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('twitter:home')
    else:
        form = UserCreationForm()
    return render(request, 'twitter/signup.html', {'form': form})

def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('twitter:home')
    else:
        form = AuthenticationForm()
    return render(request, 'twitter/login.html', {'form': form})

def home(request):
    return render(request, 'twitter/home.html')
