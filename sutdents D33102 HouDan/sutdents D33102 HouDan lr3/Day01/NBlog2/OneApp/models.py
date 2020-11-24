from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class UserDriver(AbstractUser):
    passport = models.PositiveIntegerField(null=False)
    address = models.CharField(max_length=100,null=True,blank=True)
    Citizenship = models.CharField(max_length=30,null=True,blank=True)

class driver(models.Model):
    first_name = models.CharField(max_length=30, db_column="first name")
    last_name = models.CharField(max_length=30, db_column="last name")
    birthday = models.DateTimeField(null=True)
    Driver_self = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "driver"


class driver_license(models.Model):
    license_number = models.CharField(max_length=10)
    Date_issue = models.DateTimeField()
    Driver_type = (('A', 'Motorcycle'), ('B', 'car'), ('C', 'truck'), ('D', 'bus'))
    driver_type = models.CharField(max_length=1, choices=Driver_type)
    driver_license_driver = models.OneToOneField(driver, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "driver license"


class Car(models.Model):
    Car_type_list = (('A', 'Motorcycle'), ('B', 'car'), ('C', 'truck'), ('D', 'bus'))
    Brand = models.CharField(max_length=30)
    Colour = models.CharField(max_length=30)
    state_number = models.CharField(max_length=3, db_column="state number")
    Car_type = models.CharField(max_length=1, choices=Car_type_list, db_column="Car type")

    class Meta:
        db_table = "Car"


class Ownership(models.Model):
    Ownership_day = models.DateTimeField()
    owner = models.ForeignKey(driver, null=True, blank=True, on_delete=models.SET_NULL)
    OW_Car = models.ForeignKey(Car, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "Ownership"
