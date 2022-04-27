drop table if exists Users;
CREATE TABLE Users (
	username BIGINT (10) NOT NULL,
	pwd VARCHAR (30) NOT NULL,
	category boolean NOT NULL,
	PRIMARY KEY (username)
);

drop table if exists Vehicle;
CREATE TABLE `Vehicle` (
	`Car_no` bigint(10) NOT NULL,
	`Car_Model` VARCHAR (30) NOT NULL,
	`Car_Type` VARCHAR (30) NOT NULL,
	PRIMARY KEY (`Car_no`)
);

drop table if exists Driver;
CREATE TABLE Driver (
	`Driver_id` BIGINT (10) NOT NULL,
	`Driver_Name` VARCHAR (30) NOT NULL,
	`Driver_License_No` BIGINT (10) NOT NULL,
	`Date_of_Birth` DATE NOT NULL,
	`Contact_number` BIGINT (30) NULL,
	`Rating` INT NULL,
	`Cab_location` VARCHAR (30) NOT NULL,
	`Current_status` VARCHAR(10) NOT NULL,
	`Driver_Car_Number` BIGINT(10) NOT NULL,
	PRIMARY KEY (`Driver_id`),
    FOREIGN KEY(`Driver_Car_Number`)references vehicle(`Car_no`) on delete cascade on update cascade
);

drop table if exists Passenger;
CREATE TABLE Passenger (
	`Passenger_ID` BIGINT (10) NOT NULL,
	`Name` VARCHAR (30) NOT NULL,
	`Date_of_Birth` DATE NOT NULL,
	`Contact_Number` BIGINT (10) NOT NULL,
	`Pickup_Location` VARCHAR (30) NULL,
	PRIMARY KEY (`Passenger_ID`)
);

drop table if exists Booking;
CREATE TABLE `booking` (
	`Drop_Location` VARCHAR (45) NOT NULL,
	`Pickup_Location` VARCHAR (45) NOT NULL,
	`Request_Passenger_ID` BIGINT (10) NOT NULL UNIQUE,
	`Request_Driver_ID` BIGINT (10) NOT NULL,
	PRIMARY KEY (`Request_Passenger_Id`),
    foreign key(Request_Passenger_ID) references passenger(Passenger_ID) on delete cascade on update cascade
);

drop table if exists Trip;
CREATE TABLE `Trip` (
	`Trip_ID` BIGINT (10) NOT NULL,
	`Trip_Status` VARCHAR (30) NOT NULL,
	`Trip_Date_Day` DATE NOT NULL,
	`Trip_Passenger_ID` BIGINT (10) NOT NULL ,
	`Trip_Driver_ID` BIGINT (10) NOT NULL,
	`Drop_Location` VARCHAR (45) NOT NULL,
	`Pickup_Location` VARCHAR (45) NOT NULL,
	PRIMARY KEY (`Trip_ID`)
);

drop table if exists Payment;
CREATE TABLE `Payment` (
    Trip_Id_Pay bigint(10) NOT NULL,
	`Payment_ID` BIGINT (12) NOT NULL UNIQUE,
	`Payment_Type` VARCHAR (30) NOT NULL,
	`Payment_Amount` BIGINT (5) NOT NULL,
	`Payment_Status` VARCHAR(10) NOT NULL,
    Primary Key(Trip_Id_Pay), 
    foreign key(Trip_Id_Pay) references trip(Trip_Id) ON DELETE CASCADE
);