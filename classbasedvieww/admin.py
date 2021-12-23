from django.contrib import admin

# Register your models here.
from .models import Student

@admin.register(Student)
class StudentNewModel(admin.ModelAdmin):
    list_display = ["name" , "rollno"]