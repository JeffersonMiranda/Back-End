from django.conf.urls import url
from app.views import login
from django.contrib import admin

uripatterns = {
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include('admin.site.urls')),
	url('login',login),
	url('sign',sign),
}
