from django.contrib import admin

# Register your models here.
from .models import Student,Teacher,Contractor,MBAStudent,ExamCenter,MyExamCenter

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id","name","age","fees"]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["id","name","age","salary","date"]


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ["id","name","age","payment","date"]



@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ["id","cname","city"]


@admin.register(MBAStudent)
class MBAStudentAdmin(admin.ModelAdmin):
    list_display = ["id","cname","city","name","roll"]


@admin.register(MyExamCenter)
class MyExamCenterAdmin(admin.ModelAdmin):
    list_display = ["id","cname","city"]
