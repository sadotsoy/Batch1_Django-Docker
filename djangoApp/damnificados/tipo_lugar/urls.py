from django.conf.urls import url
from .views import PersonasApi

urlpatterns=[
    url(r'^$',PersonasApi.as_view())
]
