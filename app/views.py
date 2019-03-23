from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import *
from .form import *

def welcome(request):
    return render(request, 'master/index.html')

def post(request):
    comm = Comment.objects.all()

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.user = request.user
            add.save()
            return redirect('post')
    else:
        form = CommentForm()
    return render(request,'post.html',{'form':form,'comm':comm})

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

def profile(request):
    prof = Profile.objects.filter(user=request.user)
    return render(request, 'profile/profile.html',{'prof':prof})

def editprofile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.save()
            return HttpResponse("Profile has been updated successfully")
    else:
        form = ProfileForm()
    return render(request,'profile/edit_profile.html',{'form':form})

def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        proj = Business.search_business(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'proj':proj})
    else:
        message = 'Enter term to search'
        return render(request, 'search.html', {'message':message})
