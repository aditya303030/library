from asyncio.windows_events import NULL
from django.db import models

# Create your models here.

class Book_register(models.Model):
  name_of_uploader = models.CharField(max_length=50)
  book_name = models.CharField(max_length=50)
  author = models.CharField(max_length=50)
  number_of_pages = models.IntegerField()
  brief_description = models.CharField(max_length=150)
  rating = models.IntegerField(default=0)
  review = models.CharField(max_length=120)
  class Meta:
    db_table = "Registered_books"

class Book_issue(models.Model):
  book_issue = models.CharField(max_length=50, default=None)
  date_issue = models.DateField()
  class Meta:
    db_table = "Book_Issued"