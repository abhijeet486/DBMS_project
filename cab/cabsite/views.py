import imp
from random import randint
from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
from django.db import connection
from matplotlib.style import context
from cabsite.users import *
from cabsite.helpers import *
from datetime import datetime

user_mysql='default'

def warning(request):
    return HttpResponse("Invalid credentials")

def login(request):
    print("login")
    return render(request,'DBMS/login.html',{})

def logout(request):
    with connection.cursor() as cursor:
        query = """Drop view if exists User, Dashboard ,PreviousTrips;"""
        cursor.execute(query)
    return login(request)

def showrequest(request):
    context_={}
    if request.method == 'POST':
        pk = request.POST.get("username")
        with connection.cursor() as cursor:
            query = """Select * from User;"""
            cursor.execute(query)
            data = cursor.fetchall()
            context={}
            cols = [ col[0] for col in cursor.description]
            tab = getdf(context,cols,data)
            if tab["status"][0]=='FALSE':
                cursor.execute("""Select * from booking ;""")
                req = cursor.fetchall()
                cols = [ col[0] for col in cursor.description]
                # tab["request_list"] = getdf({},cols,req)
                tab_data = getdf({},cols,req)
                for i in tab_data:
                    tab[i] = tab_data[i]
                # for i in tab:
                #     print(i,len(tab[i]))
            else:
                cursor.execute("""Select * from Dashboard ;""")
                req = cursor.fetchall()
                cols = [ col[0] for col in cursor.description]
                tab_data = getdf({},cols,req)
                for i in tab_data:
                    tab[i] = tab_data[i]
    return render(request,'DBMS/driver_booking_requests.html',context=tab)

def acceptrequest(request):
    context_={}
    if request.method == 'POST':
        pk = request.POST.get("username")
        with connection.cursor() as cursor:
            query = """Select * from User;"""
            cursor.execute(query)
            data = cursor.fetchall()
            context={}
            cols = [ col[0] for col in cursor.description]
            tab = getdf(context,cols,data)
            if tab["status"][0]=='FALSE':
                passenger_id = request.POST.get("passengerid")
                query="""Select * from booking where Request_Passenger_ID={} ;"""
                query=query.format(passenger_id)
                cursor.execute(query)
                req = cursor.fetchall()
                print(req)
                pick_loc = req[0][1]
                drop_loc = req[0][0]
                cols = [ col[0] for col in cursor.description]
                tab["request_list"] = getdf({},cols,req)
                # pick_loc = tab["request_list"]["Pickup_Location"][0]
                # drop_loc = tab["request_list"]["Drop_Location"][0]
                dt = datetime.now()
                date_day = "{}-{}-{}".format(dt.year,dt.strftime('%m'),dt.day)
                query = """Select Trip_ID from Trip ;"""
                query = query.format()
                cursor.execute(query)
                tripidlist = cursor.fetchall()[0]
                print(tripidlist)
                while(True):
                    tripid = randint(1000000000,9999999999)
                    if tripid not in tripidlist:
                        break
                query = """Insert into Trip(Trip_ID,Trip_Status,Trip_Date_Day,Trip_Passenger_ID,Trip_Driver_ID,Drop_Location,Pickup_Location) values({},'FALSE','{}',{},{},'{}','{}');"""
                query = query.format(tripid,date_day,passenger_id,pk,drop_loc,pick_loc)
                cursor.execute(query)
                # query ="""Delete from booking where Request_Passenger_ID={}"""
                # query = query.format(passenger_id)
                # cursor.execute(query)
                # query = """UPDATE driver SET Current_status = 'TRUE' WHERE (Driver_id = '{}');"""
                # query = query.format(pk)
                # cursor.execute(query)
                # query = """Update Passenger SET status='TRUE' where Passenger_ID = '{}';"""
                # query = query.format(passenger_id)
                # cursor.execute(query)
                tab["status"][0]=='TRUE'
    return render(request,'DBMS/driver_booking_requests.html',context=tab)

def booking(request):
    context={}
    if request.method == 'POST':
        pk = request.POST.get("username")
        print(pk)
        with connection.cursor() as cursor:
            query = """Select * from User;"""
            cursor.execute(query)
            data = cursor.fetchall()
            context={}
            cols = [ col[0] for col in cursor.description]
            tab = getdf(context,cols,data)
            query = """Select count(*) from booking where Request_Passenger_ID={} ;"""
            query = query.format(pk)
            cursor.execute(query)
            data = cursor.fetchall()
            print(data)
            if data[0][0]>0:
                tab["progress"]=1
            print(tab)
    return render(request,'DBMS/booking.html',context=tab)

def bookingrequest(request):
    context={}
    if request.method == 'POST':
        pk = request.POST.get("username")
        print(pk)
        with connection.cursor() as cursor:
            drop_loc = request.POST.get("drop_location")
            pick_loc = request.POST.get("pickup_location")
            query = """Select * from booking where Request_Passenger_ID={}; """
            query = query.format(pk)
            cursor.execute(query)
            data = cursor.fetchall()
            print(data)
            if data==():
                query ="""INSERT INTO booking (Drop_Location, Pickup_Location, Request_Passenger_ID) VALUES ('{}', '{}', '{}');"""
                query = query.format(drop_loc,pick_loc,pk)
                cursor.execute(query)
    return booking(request)

def customer(request):
    if request.method == 'POST':
        pk = request.POST.get("username")
        print(pk)
        with connection.cursor() as cur:
            query = """Create or Replace view User as 
            Select Passenger_ID as username,Name,status,1 as usertype from Passenger where passenger_id="{}"; """
            query = query.format(pk)
            cur.execute(query)
            query = """Select * from User;"""
            cur.execute(query)
            data = cur.fetchall()
            if data==None or data ==():
                return warning(request)
            cols = [ col[0] for col in cur.description ]
            #  ["passenger_id","name","date_of_birth","contact_number","pickup_location","status"] 
            context={}
            tab = getdf(context,cols,data)
            if tab["status"][0]=='TRUE':
                query = """ Create or Replace view Dashboard as
                 Select b.Pickup_Location,b.Drop_Location,Driver_Name as RefName,Contact_number as contactno,Driver_Car_Number from (Select Pickup_Location,Drop_Location,Trip_Driver_ID from trip join user on username=Trip_Passenger_ID where Trip_Status='FALSE') as b join driver on b.Trip_Driver_ID = Driver_id  ;"""
                print(query)
                cur.execute(query)
                query="""Select * from Dashboard;"""
                cur.execute(query)
                data = cur.fetchall()
                cols = [ col[0] for col in cur.description ]
                tab_data = getdf({},cols,data)
                for i in tab_data:
                    tab[i] = tab_data[i]
            print(tab)
        return render(request,'DBMS/customer.html',context=tab)

def driver(request):
    if request.method == 'POST' :
        pk = request.POST.get("username")
        print(pk)
        with connection.cursor() as cur:
            query = """Create or Replace view User as 
            Select Driver_id as username,Driver_Name as Name,current_status as status,0 as usertype from Driver where Driver_id="{}"; """
            query = query.format(pk)
            cur.execute(query)
            query = """Select * from User;"""
            cur.execute(query)
            data = cur.fetchall()
            print(data)
            if data==None or data ==():
                return warning(request)
            cols = [ col[0] for col in cur.description]
            # ["Driver_id","Driver_Name","Driver_License_No","Date_of_Birth","Contact_number","Rating","Cab_location","Current_status","Driver_Car_Number"] 
            context={}
            tab = getdf(context,cols,data)
            if tab["status"][0]=='TRUE':
                query = """ Create or Replace view Dashboard as
                Select b.Pickup_Location,b.Drop_Location,p.Name as RefName,p.Contact_Number as contactno from ( Select Pickup_Location,Drop_Location,Trip_Passenger_ID from trip join user on username=Trip_Driver_ID where Trip_Status='FALSE') as b join passenger p on b.Trip_Passenger_ID = p.Passenger_ID ; """
                cur.execute(query)
                print(query)
                query="""Select * from Dashboard;"""
                cur.execute(query)
                data = cur.fetchall()
                cols = [ col[0] for col in cur.description ]
                print(cols)
                print(data)
                new_data= getdf({},cols,data)
                for i in new_data:
                    tab[i] = new_data[i]
            print(tab)
        return render(request,'DBMS/driver.html',context=tab)

def editdriver(request):
    if request.method =='POST':
        pk = request.POST.get("username")
        with connection.cursor() as cursor:
            cursor.execute("""Select username,Name from User;""")
            data = cursor.fetchall()
            context={}
            cols =["username","Name"]
            tab = getdf(context,cols,data)
    return render(request,'DBMS/edit_driver.html',context=tab)

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
            dname= dname[0][0]
    return render(request,'DBMS/editpassenger.html',{"username":pk,"name":dname})

def payment(request):
    return render(request,'DBMS/payment.html',{})

def previoustrips(request):
    contex={}
    if request.method == 'POST':
        pk = request.POST.get("username")
        print(pk)
        with connection.cursor() as cursor:
            query = """Select Name,usertype from User;"""
            cursor.execute(query)
            data = cursor.fetchall()
            val = data[0][0]
            ty = data[0][1]
            query = """Create or Replace view PreviousTrips as
            Select * from Trip join Payment on Trip_Id_Pay=Trip_ID where {}={} and Trip_Status='TRUE';"""
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
            contex["displayname"] = val
            contex["usertype"] = ty
            contex["username"] = pk
        print(contex)
    return render(request,'DBMS/previoustrips.html',context=contex)
    # trip id, passenger name/driver name, contact no,

def Mangevehicles(request):
    if request.method == 'POST':
        pk = request.POST.get("username")
        with connection.cursor() as cursor:
            query = """Create or Replace view ManageVehicles as
            Select d.Driver_id as username,d.Driver_Name as Name,v.car_no,v.car_type,v.car_model from Driver d,Vehicle v where d.Driver_id="{}" and d.Driver_Car_Number=v.car_no;"""
            query=query.format(int(pk))
            cursor.execute(query)
            query = """Select * from ManageVehicles;"""
            cursor.execute(query)
            data = cursor.fetchall()
            print(data)
            cols =["username","Name","car_no","car_model","car_type"]
            context={}
            tab = getdf(context,cols,data)
            print(tab)
    return render(request,'DBMS/Mangevehicles.html',context=tab)

def loginaccess(request):
    if request.method == 'POST':
        l_id = request.POST.get("username")
        writeinfile(l_id)
        with connection.cursor() as cursor:
            query = """Select * from users where username={};"""
            query = query.format(l_id)
            cursor.execute(query)
            user_Data = cursor.fetchall()
            print(user_Data)
            pwd = str(request.POST.get("pwd"))
            pwd = request.POST.get("pwd")
            if str(user_Data[0][1]) == pwd:
                if request.POST.get("category")=='0' and user_Data[0][2]==0:
                    user_mysql='driver'
                    return driver(request)
                elif request.POST.get("category")=='1' and user_Data[0][2]==1:
                    user_mysql='customer'
                    return customer(request)
    return warning(request)