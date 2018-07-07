from django.urls import path, include
from . import views

urlpatterns = [
    path('logout', views.logout, name = 'logout'),
    path('login', views.login, name = 'lgoin'),
    path('signup', views.signup, name = 'signup'),
]
