use dbms;

create index pickuplocation
on booking(Pickup_Location);


create index droplocation
on booking(Drop_Location);


create index passengerid
on trip(Trip_Passenger_ID);

create index driverid
on trip(Trip_Driver_ID);

create index name
on passenger(Name);

create index contact_no
on passenger(Contact_Number);

create index driver_name
on driver(Driver_Name);

create index contact_no
on driver(Contact_Number);


create index Request_passid
on booking(Request_Passenger_ID);

create index Request_drive_id
on booking(Request_Driver_ID);

create index usertype
on userS(category);

create index car_type
on vehicle(Car_Type);

create index status
on driver(Current_Status);