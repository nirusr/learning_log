"""Define URL patterns for Users"""

from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import logout_view
from .views import register
app_name = "users"
urlpatterns= [
    url(r'^login/$', auth_views.LoginView.as_view(
        template_name = 'users/login.html'
    ),  name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^register/$', register, name='register'),

]

