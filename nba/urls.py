# encoding: utf-8

from django.conf.urls import url,include
from nba import views

from tastypie.api import Api
from nba.resources import TeamResource,PlayerResource


v1_api = Api(api_name='v1')
v1_api.register(TeamResource())
v1_api.register(PlayerResource())


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/', include(v1_api.urls)),
]
