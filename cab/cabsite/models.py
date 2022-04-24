# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class Booking(models.Model):
#     drop_location = models.CharField(db_column='Drop_Location', max_length=45)  # Field name made lowercase.
#     pickup_location = models.CharField(db_column='Pickup_Location', max_length=45)  # Field name made lowercase.
#     request_passenger = models.OneToOneField('Passenger', models.DO_NOTHING, db_column='Request_Passenger_ID', primary_key=True)  # Field name made lowercase.
#     request_driver = models.OneToOneField('Driver', models.DO_NOTHING, db_column='Request_Driver_ID')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'booking'
#         unique_together = (('request_passenger', 'request_driver'),)


# class Driver(models.Model):
#     driver_id = models.BigIntegerField(db_column='Driver_id', primary_key=True)  # Field name made lowercase.
#     driver_name = models.CharField(db_column='Driver_Name', max_length=30)  # Field name made lowercase.
#     driver_license_no = models.BigIntegerField(db_column='Driver_License_No')  # Field name made lowercase.
#     date_of_birth = models.DateField(db_column='Date_of_Birth')  # Field name made lowercase.
#     contact_number = models.BigIntegerField(db_column='Contact_number', blank=True, null=True)  # Field name made lowercase.
#     rating = models.IntegerField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.
#     cab_location = models.CharField(db_column='Cab_location', max_length=30)  # Field name made lowercase.
#     current_status = models.CharField(db_column='Current_status', max_length=10)  # Field name made lowercase.
#     driver_car_number = models.ForeignKey('Vehicle', models.DO_NOTHING, db_column='Driver_Car_Number')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'driver'


# class Passenger(models.Model):
#     passenger_id = models.BigIntegerField(db_column='Passenger_ID', primary_key=True)  # Field name made lowercase.
#     name = models.CharField(db_column='Name', max_length=30)  # Field name made lowercase.
#     date_of_birth = models.DateField(db_column='Date_of_Birth')  # Field name made lowercase.
#     contact_number = models.BigIntegerField(db_column='Contact_Number')  # Field name made lowercase.
#     pickup_location = models.CharField(db_column='Pickup_Location', max_length=30, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'passenger'


# class Payment(models.Model):
#     trip_id_pay = models.OneToOneField('Trip', models.DO_NOTHING, db_column='Trip_Id_Pay', primary_key=True)  # Field name made lowercase.
#     payment_id = models.BigIntegerField(db_column='Payment_ID', unique=True)  # Field name made lowercase.
#     payment_type = models.CharField(db_column='Payment_Type', max_length=30)  # Field name made lowercase.
#     payment_amount = models.BigIntegerField(db_column='Payment_Amount')  # Field name made lowercase.
#     payment_status = models.CharField(db_column='Payment_Status', max_length=10)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'payment'


# class Trip(models.Model):
#     trip_id = models.BigIntegerField(db_column='Trip_ID', primary_key=True)  # Field name made lowercase.
#     trip_status = models.CharField(db_column='Trip_Status', max_length=30)  # Field name made lowercase.
#     trip_date_day = models.DateField(db_column='Trip_Date_Day')  # Field name made lowercase.
#     trip_passenger = models.ForeignKey(Booking, models.DO_NOTHING, db_column='Trip_Passenger_ID')  # Field name made lowercase.
#     trip_driver = models.ForeignKey(Booking, models.DO_NOTHING, db_column='Trip_Driver_ID')  # Field name made lowercase.
#     drop_location = models.CharField(db_column='Drop_Location', max_length=45)  # Field name made lowercase.
#     pickup_location = models.CharField(db_column='Pickup_Location', max_length=45)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'trip'


# class Vehicle(models.Model):
#     car_no = models.BigIntegerField(db_column='Car_no', primary_key=True)  # Field name made lowercase.
#     car_model = models.CharField(db_column='Car_Model', max_length=30)  # Field name made lowercase.
#     car_type = models.CharField(db_column='Car_Type', max_length=30)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'vehicle'
