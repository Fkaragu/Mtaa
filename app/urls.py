from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^$',views.welcome),
    url(r'^registrations/',views.register),
    url(r'^profile/',views.profile),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile')
]
