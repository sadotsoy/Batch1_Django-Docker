from django.conf.urls import url
from .views import UsersApi
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns=[
    url(r'^/register$',UsersApi.as_view()),
    url(r'^login/', obtain_jwt_token),
    url(r'^token-refresh/', refresh_jwt_token),
    url(r'^token-verify/', verify_jwt_token)
]
