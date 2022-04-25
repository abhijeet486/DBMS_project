from turtle import colormode
from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
from django.db import connection
from matplotlib.style import context
from sympy import re
from websockets import Data
from cabsite.users import *
from cabsite.helpers import *

def warning(request):
    return HttpResponse("Invalid credentials")

def login(request):
    print("login")
    return render(request,'DBMS/login.html',{})

def booking(request):
    return render(request,'DBMS/booking.html',{})

def customer(request,pk):
    with connection.cursor() as cur:
        query = """Select * from Passenger where passenger_id="{}"; """
        query = query.format(pk)
        cur.execute(query)
        data = cur.fetchall()
        cols = ["passenger_id","name","date_of_birth","contact_number","pickup_location","status"] 
        context={}
        tab = getdf(context,cols,data)
        print(tab)
    return render(request,'DBMS/customer.html',context=tab)

def driver(request, pk):
    with connection.cursor() as cur:
        query = """Select * from Driver where driver_id="{}"; """
        query = query.format(pk)
        cur.execute(query)
        data = cur.fetchall()
        print(data)
        cols = ["driver_id","driver_name","driver_license_no","date_of_birth","contact_number","rating","cab_location","current_status","driver_car_number"] 
        context={}
        tab = getdf(context,cols,data)
    return render(request,'DBMS/driver.html',context=tab)

def edit_driver(request):
    return render(request,'DBMS/edit_driver.html',{})

def editpassenger(request):
    return render(request,'DBMS/editpassenger.html',{})

def payment(request):
    return render(request,'DBMS/payment.html',{})

def previoustrips(request):
    return render(request,'DBMS/previoustrips.html',{})

def Mangevehicles(request):
    if request.method == 'POST':
        pk = request.POST.get("driver_id")
        with connection.cursor() as cursor:
            query = """Create or Replace view ManageVehicles as
            Select d.driver_name,v.car_no,v.car_type,v.car_model from Driver d,Vehicle v where d.driver_id="{}" and d.driver_car_number=v.car_no;"""
            query=query.format(int(pk[1:-1]))
            cursor.execute(query)
            query = """Select * from ManageVehicles;"""
            cursor.execute(query)
            data = cursor.fetchall()
            print(data)
            cols =["driver_name","car_no","car_model","car_type"]
            context={}
            tab = getdf(context,cols,data)
            print(tab)
    return render(request,'DBMS/Mangevehicles.html',context=tab)

def loginaccess(request):
    if request.method == 'POST':
        l_id = request.POST.get("username")
        writeinfile(l_id)
        if l_id in user_id_pwd:
            if user_id_pwd[l_id] == request.POST["pwd"]:
                    if request.POST.get("category")=='0':
                        return driver(request,l_id)
                    elif request.POST.get("category")=='1':
                        return customer(request,l_id)
    return warning(request)