from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import TweetForm
from .models import Tweet
import logging

logger = logging.getLogger('django')

def index(request):
    if request.user.is_authenticated:
        return redirect('twitter:home')
    return render(request, 'twitter/index.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('twitter:home')
    else:
        form = UserCreationForm()
    return render(request, 'twitter/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('twitter:home')
    else:
        form = AuthenticationForm()
    return render(request, 'twitter/login.html', {'form': form})

@login_required
def home(request):
    if request.method == 'POST':
        form = TweetForm(data=request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.auth_user = request.user
            tweet.published_date = timezone.now()
            tweet.save() 
            return redirect('twitter:home')
    else:
        form = TweetForm()
    return render(request, 'twitter/home.html', {'form': form, 'tweets': Tweet.objects.all(), 'username': request.user.username, 'num_tweets': Tweet.objects.filter(auth_user=request.user).count()})

def usertweets(request, username):
    user = User.objects.get(username=username)
    tweets = Tweet.objects.filter(auth_user=user)
    return render(request, 'twitter/usertweets.html', {'tweets': tweets, 'username': username, 'num_tweets': tweets.count()})

def logout(request):
    auth_logout(request)
    return redirect('twitter:index')
