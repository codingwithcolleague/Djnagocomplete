from django.db import models
from django.db.models.aggregates import Max

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200)
    rollno = models.IntegerField(null=True,blank=True)
    emailId = models.CharField(max_length=100)
    mobileno = models.IntegerField(null=True,blank=True)
    passout = models.CharField(max_length=200)
    passoutdate = models.DateField()
