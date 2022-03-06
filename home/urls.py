from unicodedata import name
from django.urls import path
from . import views
from home.views import *

urlpatterns = [
    path('',views.home, name="home"),
    path('book_register',views.book_register,name='book_register'),
    path('issue_book', views.issue_book,name="issue_book"),
    path('book_issued_details',views.book_issued_details,name="book_issued_details")
]