from django.db import models
from driverAPI.models import Driver
# Create your models here.
from django.db.models import DecimalField


class Passenger(models.Model):
    """
    Stores passenger info
    """
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    number = models.IntegerField(unique=True)


class TravelHistory(models.Model):
    passenger_id = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    source_address = models.TextField()
    destination_address = models.TextField()
    booked_time = models.DateTimeField(auto_now_add=True)
car_no = models.CharField(max_length=50)
