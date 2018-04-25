from django.conf.urls import url

from . import views

app_name = 'api'

urlpatterns = [
    url(r'^login/$',
        views.login,
        name="login"),
    url(r'^registration/$',
        views.registration,
        name="registration"),
    url(r'^activate_user/(?P<activation_token>.*)/$',
        views.validate_user,
        name="validate_user")
]
