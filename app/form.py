from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text = 'Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic','bio','NeighName','contact')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('photo','comment',)

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ('user','name','location','occupants')

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('photo','name','email','user','neighbourhood')
