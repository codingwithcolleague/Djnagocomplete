from abc import abstractmethod
from django.db import models
from django.db.models.fields import proxy

# Create your models here.
class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    date = models.DateField()
    class Meta:
        abstract = True

class Student(CommonInfo):
    fees = models.IntegerField()
    date = None

class Teacher(CommonInfo):
    salary = models.IntegerField()

class Contractor(CommonInfo):
    date = models.DateTimeField()
    payment = models.IntegerField()

"""
    MultiTable Inheritance
"""

class ExamCenter(models.Model):
    cname = models.CharField(max_length=70)
    city = models.CharField(max_length=70)


class MBAStudent(ExamCenter):
    name = models.CharField(max_length=200)
    roll = models.IntegerField()

# class ExamCneter(models.Model):
#     cname = models.CharField(max_length=200)
#     city = models.CharField(max_length=300)

class MyExamCenter(ExamCenter):
    class Meta:
        proxy = True


