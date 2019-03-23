from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.welcome),
    url(r'^profile/',views.profile),
    url(r'^post/',views.post, name='post'),
    url(r'^registrations/',views.register),
    url(r'^search/',views.search, name='search'),
    url(r'^editprofile/',views.editprofile, name='editprofile'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^neighbourhood/',views.neighbourhood, name='neighbourhood')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
