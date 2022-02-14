from unicodedata import name
from django.urls import path
from . import views
from .views import *

urlpatterns = [
  path('sign-in',views.sign_in,name = 'sign-in'),
  path('sign-up',views.sign_up,name = 'sign-up'),
  path('logout', views.logout, name="logout")
]
