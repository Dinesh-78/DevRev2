from django.urls import path

from . import views
from .views import Login, logoutuser, Register, HomePage, search

urlpatterns = [
    path('', HomePage, name="home-page"),
    path('register/', Register, name="register-page"),
    path('login/', Login, name="login-page"),
    path('logout/', logoutuser, name='logout'),
    path('search/', search, name="search"),
]
