from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Doctor(models.Model):
    Name = models.CharField(max_length=20,)
    phone = models.IntegerField()
    special = models.CharField(max_length=200)


    def __str__(self):
        return str(self.user)
    

class Patient(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=12)
    mobile = models.IntegerField(null=True)
    address =models.TextField()

    def __str__(self):
        return str(self.user)
    
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

