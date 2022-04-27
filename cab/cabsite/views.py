from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
from django.db import connection
from cabsite.users import *
from cabsite.helpers import *

def warning(request):
    return HttpResponse("Invalid credentials")

def login(request):
    print("login")
    return render(request,'DBMS/login.html',{})

def logout(request):
    with connection.cursor() as cursor:
        query = """Drop view if exists User;"""
        cursor.execute(query)
    return login(request)

def booking(request):
    return render(request,'DBMS/booking.html',{})

def bookingrequest(request):
    return render(request,'DBMS/driver.html',{'request':1})

def customer(request):
    if request.method == 'POST':
        pk = request.POST.get("username")
        print(pk)
        with connection.cursor() as cur:
            query = """Create or Replace view User as 
            Select *,1 as usertype from Passenger where passenger_id="{}"; """
            query = query.format(pk)
            cur.execute(query)
            query = """Select Passenger_ID,Name,status from User;"""
            cur.execute(query)
            data = cur.fetchall()
            if data==None or data ==():
                return warning(request)
            cols = [ col[0] for col in cur.description ]
            #  ["passenger_id","name","date_of_birth","contact_number","pickup_location","status"] 
            context={}
            tab = getdf(context,cols,data)
            print(tab)
        return render(request,'DBMS/customer.html',context=tab)

def driver(request):
    if request.method == 'POST' :
        pk = request.POST.get("username")
        print(pk)
        with connection.cursor() as cur:
            query = """Create or Replace view User as 
            Select *,0 as usertype from Driver where Driver_id="{}"; """
            query = query.format(pk)
            cur.execute(query)
            query = """Select Driver_id,Driver_Name,current_status from User;"""
            cur.execute(query)
            data = cur.fetchall()
            print(data)
            if data==None or data ==():
                return warning(request)
            cols = [ col[0] for col in cur.description]
            # ["Driver_id","Driver_Name","Driver_License_No","Date_of_Birth","Contact_number","Rating","Cab_location","Current_status","Driver_Car_Number"] 
            context={}
            tab = getdf(context,cols,data)
        return render(request,'DBMS/driver.html',context=tab)

def editdriver(request):
    if request.method =='POST':
        pk = request.POST.get("username")
        with connection.cursor() as cursor:
            cursor.execute("""Select Driver_Name from User;""")
            name = cursor.fetchall()
            name = name[0][0]
    return render(request,'DBMS/edit_driver.html',{"username":pk,"name":name})

def savechanges(request):
    pk = request.POST.get("username")
    ty = None
    if request.method == 'POST' and user_id_pwd[pk] == request.POST["pwd"]:
        with connection.cursor() as cursor:
            query="""Select usertype from User;"""
            cursor.execute(query)
            ty = cursor.fetchall()
            ty = ty[0][0]
            print(ty)
            if ty==0:
                name=request.POST.get("name")
                if name!=None and name!="":
                    query = """UPDATE driver SET Driver_Name = '{}' WHERE (Driver_id = '{}');"""
                    query = query.format(name,pk)
                    cursor.execute(query)
                license_no=request.POST.get("license_no")
                if license_no!=None and license_no!="":
                    query = """UPDATE driver SET Driver_License_No = '{}' WHERE (Driver_id = '{}');"""
                    query = query.format(license_no,pk)
                    cursor.execute(query)
                dob=request.POST.get("dob")
                if dob!=None and dob!="":
                    query = """UPDATE driver SET Date_of_Birth = '{}' WHERE (Driver_id = '{}');"""
                    query = query.format(dob,pk)
                    print(query)
                    cursor.execute(query)
                contact=request.POST.get("contact")
                if contact!=None and contact!="":
                    query = """UPDATE driver SET Contact_number = '{}' WHERE (Driver_id = '{}');"""
                    query = query.format(contact,pk)
                    cursor.execute(query)
                location=request.POST.get("location")
                if location!=None and location!="":
                    query = """UPDATE driver SET Cab_location = '{}' WHERE (Driver_id = '{}');"""
                    query = query.format(location,pk)
                    cursor.execute(query)
            else:
                name=request.POST.get("name")
                if name!=None and name!="":
                    query = """Update Passenger SET Name='{}' where Passenger_ID = '{}';"""
                    query = query.format(name,pk)
                    cursor.execute(query)
                dob=request.POST.get("dob")
                if dob!=None and dob!="":
                    query = """Update Passenger SET Date_of_Birth='{}' where Passenger_ID = '{}';"""
                    query = query.format(dob,pk)
                    cursor.execute(query)
                contact=request.POST.get("contact")
                if contact!=None and contact!="":
                    query = """Update Passenger SET Contact_Number='{}' where Passenger_ID = '{}';"""
                    query = query.format(contact,pk)
                    cursor.execute(query)
                # location=request.POST.get("location")
                # if location!=None or location!="":
                #     query = """Update Passenger SET Pickup_Location='{}' where Passenger_ID = '{}';"""
                #     query = query.format(location,pk)
                #     cursor.execute(query)
        loginaccess(request)
    if ty==0:
        return editdriver(request)
    return editpassenger(request)

def editpassenger(request):
    pk=None
    dname=None
    if request.method=='POST':
        pk = request.POST.get("username")
        with connection.cursor() as cursor:
            cursor.execute("""Select Name from User;""")
            dname = cursor.fetchall()
            dname=dname[0][0]
    return render(request,'DBMS/editpassenger.html',{"username":pk,"name":dname})

def payment(request):
    return render(request,'DBMS/payment.html',{})

def previoustrips(request):
    contex={}
    if request.method == 'POST':
        pk = request.POST.get("username")
        print(pk)
        with connection.cursor() as cursor:
            query = """Select usertype from User;"""
            cursor.execute(query)
            ty = cursor.fetchall()
            print(ty)
            ty = ty[0][0]
            query = """Create or Replace view PreviousTrips as
            Select * from Trip where {}={} ;"""
            if ty==0:
                query = query.format("Trip_Driver_id",pk)
            else:
                query = query.format("Trip_Passenger_ID",pk)
            cursor.execute(query)
            query = """Select * from PreviousTrips;"""
            cursor.execute(query)
            data=cursor.fetchall()
            cols=[col[0] for col in cursor.description]
            contex = getdf(contex,cols,data)
            if ty == 0:
                query="""Select Driver_Name from User;"""
                cursor.execute(query)
                val = cursor.fetchall()
                contex["displayname"] = val[0][0]
            else:
                query="""Select Name from User;"""
                cursor.execute(query)
                val = cursor.fetchall()
                contex["displayname"] = val[0][0]
            contex["usertype"] = ty
        print(contex)
    return render(request,'DBMS/previoustrips.html',context=contex)
    # trip id, passenger name/driver name, contact no,

def Mangevehicles(request):
    if request.method == 'POST':
        pk = request.POST.get("Driver_id")
        with connection.cursor() as cursor:
            query = """Create or Replace view ManageVehicles as
            Select d.Driver_id,d.Driver_Name,v.car_no,v.car_type,v.car_model from Driver d,Vehicle v where d.Driver_id="{}" and d.Driver_Car_Number=v.car_no;"""
            query=query.format(int(pk))
            cursor.execute(query)
            query = """Select * from ManageVehicles;"""
            cursor.execute(query)
            data = cursor.fetchall()
            print(data)
            cols =["Driver_id","Driver_Name","car_no","car_model","car_type"]
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
                        return driver(request)
                    elif request.POST.get("category")=='1':
                        return customer(request)
    return warning(request)