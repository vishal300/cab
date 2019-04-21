from django.db import models

# Create your models here.
from django.db.models import DecimalField


class Driver(models.Model):
    """
    Storing driver details
    """
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    number = models.IntegerField(unique=True)
    license = models.CharField(max_length=80, unique=True)
    car_no = models.CharField(max_length=80, unique=True)


class DriverLocation(models.Model):
    """
    Storing Drivers Locations that are coming to server
    when driver is logged in into the application
    """
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    latitude = DecimalField(max_digits=9, decimal_places=6)
    longitude = DecimalField(max_digits=9, decimal_places=6)


class DriverRidesHistory(models.Model):
    """
    Stores ride history for drivers
    """

    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    passenger_id = models.ForeignKey('passengerAPI.Passenger', on_delete=models.CASCADE)
    source_address = models.TextField()
    destination_address = models.TextField()
    booked_time = models.DateTimeField(auto_now_add=True)
    car_no = models.CharField(max_length=80, unique=True)
passenger_name = models.CharField(max_length=80)
