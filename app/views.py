from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def welcome(request):
    return render(request, 'master/index.html')
