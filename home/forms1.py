from django import forms 
from .models import *

class BookIssueForm(forms.ModelForm):
  class Meta:
    model = Book_issue
    fields = '__all__'