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
