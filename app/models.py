from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from pyuploadcare.dj.models import ImageField

class Profile(models.Model):
    user = models.OneToOneField(User)
    profile_pic = models.ImageField(upload_to='articles/', blank=True)
    bio = models.TextField(max_length=500, blank=True)
    contact = models.TextField(max_length=500, blank=True)

    def __str_(self):
        return self.contact

    def save_profile(self):
        self.save()

class Neighbourhood(models.Model):
    name = models.TextField(max_length=30, blank=True)
    location = models.TextField(max_length=30, blank=True)
    occupants = models.TextField(max_length=30, blank=True)
    user = models.OneToOneField(User)

    def __str_(self):
        return self.name

    def neighbourhood(self):
        self.save()

class Business(models.Model):
    name = models.TextField(max_length=30, blank=True)
    user = models.ForeignKey(User)
    neighbourhood = models.ForeignKey(Neighbourhood)
    email = models.EmailField(max_length=70,blank=True)

    def __str_(self):
        return self.name

    def save_business(self):
        self.save()
