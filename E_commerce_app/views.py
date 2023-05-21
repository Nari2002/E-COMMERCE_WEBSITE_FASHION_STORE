from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from E_commerce_app.models import user
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url="login")
def ecom(request):
    return render(request,"home/index.html")
def login_user(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(ecom)
        if user is None:
            return redirect(register_user)
    return render(request,"login.html" or "signup/signup.html")
    
def register_user(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        email=request.POST.get("email")
        c=User.objects.create_user(username=username,email=email,password=password)
        c.save()
        return redirect(login_user)
    return render(request,"signup/signup.html")


