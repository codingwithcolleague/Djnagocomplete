from django.db import models
from django.db.models import base

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField(unique=True,null=False)
    city = models.CharField(max_length=200)
    marks = models.IntegerField()
    pass_date_time = models.DateTimeField(null=True)
    pass_date = models.DateField(blank=True,null=True)
