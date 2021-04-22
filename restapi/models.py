from django.db import models
from django.core.exceptions import ValidationError


def validate_digit_length(phone):
    if not len(str(phone)) == 10:    
        raise ValidationError('%(phone)s must be 10 digits')

# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50,unique=True)
    phone = models.IntegerField(validators=[validate_digit_length],unique=True)
    liscence = models.CharField(max_length=30,unique=True)
    carNumber = models.CharField(max_length=30,unique=True)
    
    
    
    
class DriverLocation(models.Model):
    long = models.DecimalField(max_digits=15, decimal_places=6)
    lat = models.DecimalField(max_digits=15, decimal_places=6)
    driver = models.ForeignKey(Driver,on_delete=models.CASCADE, null=True)
    
