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

