from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.welcome),
    url(r'^registrations/',views.register),
    url(r'^profile/',views.profile),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^editprofile/',views.editprofile, name='editprofile')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
