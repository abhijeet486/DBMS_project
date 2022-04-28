use dbms;




DELIMITER $$
CREATE  TRIGGER location_same
            AFTER INSERT
            ON booking FOR EACH ROW
            BEGIN  
              IF (NEW.Pickup_Location = New.Drop_Location)
              THEN  
              Delete from booking ;
              
END IF;
END;


DELIMITER $$
CREATE  TRIGGER check_date_of_birth
            AFTER INSERT
            ON driver FOR EACH ROW
            BEGIN  
              IF ( '2002-01-01'< NEW.Date_of_birth <'2022-12-31')
              THEN  
              Delete from driver ;
              
END IF;
END;

DELIMITER $$
CREATE  TRIGGER pay_out
            AFTER INSERT
            ON payment FOR EACH ROW
            BEGIN  
              IF (New.Payment_Amount <0)
              THEN  
              Delete from payment ;
              
END IF;
END;


DELIMITER $$
CREATE  TRIGGER SAME_CAR_NO
            AFTER UPDATE
            ON vehicle FOR EACH ROW
            BEGIN  
              IF (New.Car_no = Old.Car_no)
              THEN  
              Delete from vehicle ;
              
END IF;
END;

drop trigger if exists update_driver_status;

Create trigger update_status after insert on trip
for each row
Update passenger
set status = 'TRUE'
where New.Trip_Passenger_ID=Passenger_ID;

Create trigger update_driver_status after insert on trip
for each row
Update driver
set Current_status = 'TRUE'
where New.Trip_Driver_ID=Driver_id;

Create trigger update_booking after insert on trip
for each row 
delete from booking
where new.Trip_Passenger_ID=Request_Passenger_ID;

