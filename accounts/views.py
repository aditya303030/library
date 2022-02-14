from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate 


# Create your views here.
def sign_in(request):
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]
    user = auth.authenticate(username=username,password=password)
    if user is not None:
      auth.login(request,user)
      return redirect('/')
  return render(request, 'sign-in.html',{})

def sign_up(request):
  if request.method == "POST":
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    user = User.objects.create_user(first_name=first_name, last_name=last_name,username=username, password=password, email=email)
    user.save()
    print('user created')
    return redirect('/sign-in')
  return render(request,'sign-up.html',context = {"UserSignUp":UserSignUp})

def logout(request):
  auth.logout(request)
  return redirect('/')