from django.shortcuts import render,redirect
from app1.forms import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login_user')
def home(request):
    return render(request,'home.html')
def register(request):
    S=StudentForm()
    d={'S':S}
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'register.html',d)

def New_user(request):
    if request.method=='POST':
        N=request.POST['n']
        P=request.POST['p']
        U=User.objects.create_user(username=N,password=P)
        U.save()
        return redirect('home')
    return render(request,'New_user.html')
def login_user(request):
    if request.method=='POST':
        N=request.POST['n']
        P=request.POST['p']
        user=authenticate(username=N,password=P)
        if user is not None:
            login(request,user)
            return redirect(home)
        else:
            return redirect('New_user')
    return render(request,'login.html')
def logout_user(request):
    logout(request)
    return redirect('home')
def user_data(request):
     SS=Student.objects.all()
     d={'SS':SS}
     return render(request,'login_data.html',d)
    
