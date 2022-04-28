use dbms;

select user from mysql.user;

create user ADMIN@localhost 
IDENTIFIED BY 'SITE_ADMIN';

GRANT ALL 
ON project.*
TO ADMIN@localhost;

SHOW GRANTS FOR ADMIN@localhost;

-- create user driver;
-- create user passenger;

CREATE USER 'driver'@'localhost' IDENTIFIED BY 'driver';
CREATE USER 'passenger'@'localhost' IDENTIFIED BY 'passenger';

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

flush privileges;