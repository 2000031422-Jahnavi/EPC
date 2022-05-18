from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login

def index(request):
    return render(request, "commons.html")

def home(request):
    return render(request, "home.html")
def about(request):
    return render(request, "about.html")
def services(request):
    return render(request, "services.html")
def job(request):
    return render(request, "job.html")
def contact(request):
    return render(request, "contact.html")
def dashboard (request):
     return render(request,"dashboard.html") 
def applicationform (request):
     return render(request,"application form.html") 
def statistics (request):
     return render(request,"statistics.html") 

def newuserregister(request):
    if request.method == 'POST':
        username =request.POST['username']
        email =request.POST['email']
        password =request.POST['password']
        mobileno =request.POST['mobileno']


        if User.objects.filter(username=username):
            messages.error(request,"username is exits")
            return redirect('/')
        
        if User.objects.filter(email=email):
            messages.error(request,"email is exits")
            return redirect('/')

        if len(username)>20:
            messages.error(request,"username lessthan 20")
            return redirect('/')
        
        if not username.isalnum():
            messages.error(request,"only in alpha,numbric")
            return redirect('/')

        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()

        messages.success(request,"Your account is register succesfully created")
        return render(request,"login.html")
        

    return render(request,"newuserregister.html")

      

def login(request):
    if request.method=='POST':
        username =request.POST['username']
        password =request.POST['password']

        user=authenticate(username=username,password=password)

        if user is not None:
            auth_login(request,user)
            return render(request,"dashboard.html",)
        else:
            messages.error(request,"wrong details")
            return redirect('/')

    return render(request,"login.html")
def signout(request):
        logout(request)
        messages.success(request,"Logged out")
        
        return redirect('/')




