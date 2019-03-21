from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def welcome(request):
    return render(request, 'master/index.html')

def register(request):
    if request.user.is_authenticated():
        return render(request,'master/index.html')
    else:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = True
                user.save()
                return redirect(request, 'Login/success.html')
        else:
            form = SignupForm()
            return render(request, 'Login/signup.html',{'form':form})
