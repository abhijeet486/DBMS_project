
from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
from cabsite.users import *
from cabsite.helpers import *

def warning(request):
    return HttpResponse("Invalid credentials")

def login(request):
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
    print("here")
    l_id =  request.POST.get('emailid')
    l_id = request.POST['emailid'].strip()
    print(l_id)
    writeinfile(l_id)
    if l_id in user_id_pwd:
        if user_id_pwd[l_id] == request.POST['pwd'].strip():
            if request.POST['a']==0:
                return redirect(driver)
            elif request.POST['a']==1:
                return customer(request)
    return redirect(warning)