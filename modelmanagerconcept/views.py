from django.shortcuts import render
from .models import Student,ProxyStudent

# Create your views here.

def home(request):
    students = Student.students.get_stu_roll_range(1,120)
    students = ProxyStudent.students.get_stu_roll_range(1,120)

    return render(request,"modelmanagerconcept/home.html",{"students":students})