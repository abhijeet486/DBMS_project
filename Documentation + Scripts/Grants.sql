use dbms;

create user ADMIN
IDENTIFIED BY 'SITE_ADMIN';




SHOW GRANTS FOR ADMIN;



GRANT ALL 
ON dbms.*
TO ADMIN;



create user driver;
create user passenger;


grant select(Pickup_Location,Drop_Location) 
on booking
to passenger;

grant select(Pickup_Location,Drop_Location) 
on booking
to driver;


grant select(Payment_Status)
on payment
to driver;

grant insert(Payment_Amount,Payment_Type)
on payment
to passenger;
grant select(Driver_Name,Cab_Location)
on driver
to passenger;