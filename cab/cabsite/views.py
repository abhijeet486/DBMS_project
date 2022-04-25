
from asyncio.log import logger
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView

# Create your views here.
from cabsite.users import *
from cabsite.helpers import *

def warning(request):
    return HttpResponse("Invalid credentials")

def login(request):
    print("login")
    return render(request,'DBMS/login.html',{})

def booking(request):
    return render(request,'DBMS/booking.html',{})

def customer(request):
    return render(request,'DBMS/customer.html',{})

def driver(request):
    return render(request,'DBMS/driver.html',{})

def edit_driver(request):
    return render(request,'DBMS/edit_driver.html',{})

def editpassenger(request):
    return render(request,'DBMS/editpassenger.html',{})

def payment(request):
    return render(request,'DBMS/payment.html',{})

def previoustrips(request):
    return render(request,'DBMS/previoustrips.html',{})

def loginaccess(request):
    if request.method == 'POST':
        l_id = request.POST.get("username")
        writeinfile(l_id)
        if l_id in user_id_pwd:
            if user_id_pwd[l_id] == request.POST["pwd"]:
                if request.POST.get("category")=='0':
                    return driver(request)
                elif request.POST.get("category")=='1':
                    return customer(request)
    return warning(request)