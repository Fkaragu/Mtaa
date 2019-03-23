from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from pyuploadcare.dj.models import ImageField

class Neighbourhood(models.Model):
    name = models.TextField(max_length=30, blank=True)
    location = models.TextField(max_length=30, blank=True)
    occupants = models.TextField(max_length=30, blank=True)
    user = models.ForeignKey(User)

    def __str_(self):
        return self.name

    def neighbourhood(self):
        self.save()

    @classmethod
    def create_neigborhood(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete_neigborhood(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def update_neighborhood(self):
        db.session.update(self)
        db.session.commit()

    @classmethod
    def update_occupants(self):
        db.session.update(self)
        db.session.commit()

    @classmethod
    def find_neigborhood(cls,neigborhood_id):
        pro = Neighbourhood.objects.filter(id = neigborhood_id)
        return pro

class Profile(models.Model):
    NeighName = models.ForeignKey(Neighbourhood)
    user = models.OneToOneField(User)
    profile_pic = models.ImageField(upload_to='articles/',default='articles/NoPic.png', blank=True)
    bio = models.TextField(max_length=500, blank=True)
    contact = models.TextField(max_length=500, blank=True)

    def __str_(self):
        return self.contact

    def save_profile(self):
        self.save()

class Business(models.Model):
    photo = models.ImageField(upload_to='articles/', default='articles/NoPic.png',blank=True)
    name = models.TextField(max_length=30, blank=True)
    user = models.ForeignKey(User)
    neighbourhood = models.ForeignKey(Neighbourhood)
    email = models.EmailField(max_length=70,blank=True)

    def __str_(self):
        return self.name

    def save_business(self):
        self.save()

    @classmethod
    def create_business(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete_business(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def update_business(self):
        db.session.update(self)
        db.session.commit()

    @classmethod
    def find_business(cls,business_id):
        pro = Business.objects.filter(id = business_id)
        return pro

    @classmethod
    def search_business(cls, name):
        pro = Business.objects.filter(name__icontains = name)
        return pro

class Comment(models.Model):
    user = models.ForeignKey(User)
    photo = models.ImageField(upload_to='articles/',default='articles/default.jpg',blank=True)
    comment = models.TextField(max_length=500)
    post_date = models.DateTimeField(auto_now=True)


    def __str_(self):
        return self.comment

    def save_comment(self):
        self.save()
