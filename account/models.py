from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class patients(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
