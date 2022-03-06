import imp
from multiprocessing import context
import re
from django.shortcuts import redirect, render
from .forms import *
from .forms1 import *
from django.views.generic.edit import CreateView
# Create your views here.
def home(request):
  book_requested = Book_register.objects.all()
  books_number =Book_register.objects.all().count()
  return render(request, 'home.html', {'book_requested':book_requested,"books_number": books_number})

def book_register(request):
  BookRegister = BookRegisterForm(request.POST or None)
  if BookRegister.is_valid():
    BookRegister.save()
    return redirect('/')
  return render(request, 'book_register.html' ,context={"BookRegisterForm":BookRegisterForm})

def book_info(request):
  if request.method=="POST":
    book_name = request.POST['book_name']
    book = Book_register.objects.check(book_name=book_name)
    if book is not None:
      print('book exists')
  return render(request,'home.html',{})

def issue_book(request):
  book_requested = Book_register.objects.all()
  BookIssue = BookIssueForm(request.POST or None)
  if BookIssue.is_valid():
    BookIssue.save()
    print('Book Issued')
    return redirect('/book_issued_details')
  return render(request, 'issue_book.html',context ={'book_requested':book_requested,"BookIssueForm":BookIssueForm})

def book_issued_details(request):
  books_issued = Book_issue.objects.all()
  return render(request,'book_issued_details.html',context={'books_issued':books_issued})