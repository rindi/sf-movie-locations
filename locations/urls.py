from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'_list$', views.location_list, name='location_list'),
	url(r'^$', views.index, name='index'),
]