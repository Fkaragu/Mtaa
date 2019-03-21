from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^$',views.welcome),
    url(r'^registrations/',views.register)
]
