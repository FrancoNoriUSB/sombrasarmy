from django.conf.urls import *

#Urls para los views de los clientes
urlpatterns = patterns('sombrasarmy.apps.main.views',
	url(r'^$', 'pre_home', name='pre_home'),
)