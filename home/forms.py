from django import forms 
from .models import *

class BookRegisterForm(forms.ModelForm):
  class Meta:
    model = Book_register
    fields = '__all__'

class BookIssueForm(forms.ModelForm):
  class Meta:
    model = Book_issue
    fields = '__all__'