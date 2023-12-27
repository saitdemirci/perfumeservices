from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .models import *
from django.utils.translation import gettext as _

def home(request):
    return render(request,'index.html',{})
def contact(request):
    yourcontact = Contact.objects.all()
    return render(request,'contact.html',{'youcontact':yourcontact})
def about(request):
    if request.method == "POST":
        Contact.objects.create(
            first_name = request.POST['first-name'],
            last_name = request.POST['last-name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message'],
        )
        messages.success(request,_("Your form is submitted "))
    return render(request,'about.html',{})

def Login(request):
    if request.user.is_authenticated:
        return render(request ,'index.html')
    else:
        messages.info(request, "Please login to access this page")
        return HttpResponseRedirect('/')
    
def LoginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username , password=password)
        if user != None:
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            messages.error(request, " Enter your data correctly")
            return HttpResponseRedirect('/')
def LogOutUser(request):
    logout(request)
    request.user= None
    return HttpResponseRedirect('/')


