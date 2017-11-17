from django.conf.urls import url
from app.views import login

uripatterns = {
	url('login',login),
}
