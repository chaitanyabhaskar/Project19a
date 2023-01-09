from email import message
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
# Create your views here.
def register(request):
    if request.method=='POST':
        
        un=request.POST['username']
        em=request.POST['email']
        pa1=request.POST['password1']
        pa2=request.POST['password2']
        if pa1!=pa2:
            messages.info(request,"Passwords are not Matching")
            return redirect('register')
        if len(pa1)<8:
            messages.info(request,"Password length must be atleat 8 characters!!")
            return redirect('register')
        if User.objects.filter(username=un).exists() or User.objects.filter(email=em).exists():
            messages.info(request,'Please Use Your Own register id OR Email')
            return redirect('register')
        else:
            user=User.objects.create_user(username=un,password=pa1,email=em)
            user.save()
            messages.info(request,"Account Created Successfully!")
            return redirect('/accounts/login')
    return render(request,'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            if user.is_staff:
                return redirect('adm')
            return redirect('usr1')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'index.html')
def logout(request):
    auth.logout(request)
    return redirect('login')
    