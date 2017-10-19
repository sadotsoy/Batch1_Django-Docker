from django.conf.urls import url
from .views import PersonasApi,PersonaApi

urlpatterns=[
    url(r'^$',PersonasApi.as_view(), name='personas_endpoint'),
    url(r'(?P<pk>[0-9]+)/$',PersonaApi.as_view(), name='persona_endpoint')
]
