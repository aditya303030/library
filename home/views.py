from django.shortcuts import redirect, render
from .forms import *
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
  return render(request, 'issue_book.html',{'book_requested':book_requested})

