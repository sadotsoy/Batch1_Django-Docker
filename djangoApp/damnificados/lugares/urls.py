from django.conf.urls import url
from .views import LugaresApi, LugarApi

urlpatterns=[
    url(r'^$',LugaresApi.as_view(), name="lugares_endpoint"),
    url(r'(?P<pk>[0-9]+)/$',LugarApi.as_view(), name='lugar_endpoint')
]
