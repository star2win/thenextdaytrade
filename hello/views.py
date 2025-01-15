from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from .models import Greeting, StockTrade, UserProfile
from django.http import HttpResponseForbidden
from django.http import JsonResponse
from .utils import is_valid_ticker

import os
import requests
from django.http import HttpResponse

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect publishers and readers to their respective pages
            if user.userprofile.is_trader:
                return redirect('trader')
            else:
                return redirect('reader')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

# Protect these views with login_required decorator
#@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def db(request):
    # If you encounter errors visiting the `/db/` page on the example app, check that:
    #
    # When running the app on Heroku:
    #   1. You have added the Postgres database to your app.
    #   2. You have uncommented the `psycopg` dependency in `requirements.txt`, and the `release`
    #      process entry in `Procfile`, git committed your changes and re-deployed the app.
    #
    # When running the app locally:
    #   1. You have run `./manage.py migrate` to create the `hello_greeting` database table.

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

def logout_view(request):
    logout(request)
    return redirect('index')

def is_trader(user):
    try:
        return user.userprofile.is_trader
    except UserProfile.DoesNotExist:
        return False

@login_required(login_url='login')
@user_passes_test(is_trader)
def trader_view(request):
    if request.method == 'POST':
        trade = StockTrade(
            trader=request.user,
            ticker=request.POST['ticker'].upper(),
            price=request.POST['price'],
            trade_type=request.POST['trade_type']
        )
        trade.save()
        return redirect('trader')
    
    trades = StockTrade.objects.all()
    return render(request, 'trader.html', {'trades': trades})

@login_required(login_url='login')
def reader_view(request):
    trades = StockTrade.objects.all()
    return render(request, 'reader.html', {'trades': trades})

def validate_ticker(request):
    """API endpoint to check if a stock ticker is valid"""
    symbol = request.GET.get('symbol', '').upper()
    return JsonResponse({
        'valid': is_valid_ticker(symbol)
    })
