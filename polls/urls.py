from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<nome_local>[a-z A-Z 0-9]+)/$', views.foto, name= 'foto')
    
    ]

