from django.db import models
from django.db.models.fields import proxy
from.manager import CustomManager

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()

    # students = models.Manager()
    students = CustomManager()

class ProxyStudent(Student):
    students = CustomManager()
    class Meta:
        proxy = True
        ordering = ["name"]