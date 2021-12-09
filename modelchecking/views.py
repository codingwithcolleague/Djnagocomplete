from django.db.models.aggregates import Count
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Student
from django.db.models import Q
from datetime import date,time
from django.db.models import Avg,Min,Max,Count,Sum


# Create your views here.
def home(request):
#     studentobj = Student.objects.all()
#     studentobj = Student.objects.filter(marks='200')
#     studentobj = Student.objects.exclude(marks='200')
#     studentobj = Student.objects.order_by('marks')
#     studentobj = Student.objects.order_by('-marks')
#     studentobj = Student.objects.order_by('?') #Randomly sort
#     studentobj = Student.objects.order_by('id').reverse()[:5]
#     studentobj = Student.objects.values() # return dictnarory
    # studentobj = Student.objects.values('name')
    # studentobj = Student.objects.values_list()
    # studentobj = Student.objects.values_list('name',named=True)# name tupled
    # studentobj = Student.objects.values_list(named=True)
    # studentobj = Student.objects.using('default') #default is database name
    # studentobj = Student.objects.dates("pass_date_time" , "year")
    # studentobj = Student.objects.filter(id=1) & Student.objects.filter(roll=101)
    # studentobj = Student.objects.filter(id=1  ,roll=101)
    # studentobj = Student.objects.filter(Q(id=1) & Q(roll=101))
    # studentobj = Student.objects.filter(id=1) | Student.objects.filter(roll=1011)
    # studentobj = Student.objects.filter(Q(id=1) | Q(roll=101))
    # studentobj = Student.objects.filter(~Q(id=1) )

    studentobj = Student.objects.first()
    studentobj = Student.objects.filter(name="Sonu").first()
    try:
        studentobj = Student.objects.get(name="Sonu")
    except studentobj.MultipleObjectsReturned:
        studentobj = Student.objects.filter(name="Sonu").first()
    # studentobj = Student.objects.last()
    # studentobj = Student.objects.latest('pass_date')
    studentobj = Student.objects.all()
    print(studentobj.exists())
    print(Student.objects.filter(pk=1).exists())
    # Student.objects.create(name="Rahul",roll=123,city='Bokaro',marks=80,pass_date='2020-5-9')
    # student_data,created = Student.objects.get_or_create(name="sameer",roll=30,city="Bokaro",marks=34,pass_date="2020-9-9")
    # studentobj = Student.objects.filter(id=12).update(name='Kabir',marks=1000)
    # studentobj,created = Student.objects.update_or_create(id=4,name="Rahul", default={'name' : 'Ravi'})

    # objs =  [
    #             Student(name='Rahul',roll=23, city='Dhanabd' , marks=200, pass_date='2202-9-9'),
    #             Student(name='Ram',roll=23, city='Dhanabd' , marks=200, pass_date='2202-9-9')
    #         ]
    # objData = Student.objects.bulk_create(objs)

    # all_student_data = Student.objects.all()
    # for stu in all_student_data:
    #     stu.city = "Dhanabd"
    # studentobj = Student.objects.bulk_update(all_student_data,['city'])
    # studentobj = Student.objects.in_bulk([1,2])
    # all_student_data = Student.objects.filter(marks=50).delete()

    # all_student_data = Student.objects.all()
    # print(all_student_data.count())


    #Look Up Filter

    studentobj = Student.objects.all()
    studentobj = Student.objects.filter(name__exact='Sonam')
    studentobj = Student.objects.filter(name__iexact='Sonam')
    studentobj = Student.objects.filter(name__contains='Sonam')
    studentobj = Student.objects.filter(name__icontains='Sonam')
    studentobj = Student.objects.filter(id__in= [1,2])
    studentobj = Student.objects.filter(marks__in= [1,2])
    studentobj = Student.objects.filter(marks__gt= 60)
    studentobj = Student.objects.filter(marks__gte= 60)
    studentobj = Student.objects.filter(marks__lt= 60)
    studentobj = Student.objects.filter(marks__lte=60)
    studentobj = Student.objects.filter(marks__startswith='S')
    studentobj = Student.objects.filter(marks__istartswith='S')
    studentobj = Student.objects.filter(marks__endswith='L')
    studentobj = Student.objects.filter(marks__iendswith='L')
    studentobj = Student.objects.filter(pass_date__range=('2020-08-01','2022-10-01'))
    studentobj = Student.objects.filter(pass_date_time__date=date(2021,12,5))
    studentobj = Student.objects.filter(pass_date_time__date__gt=date(2021,1,3))
    studentobj = Student.objects.filter(pass_date__year = 2021)
    studentobj = Student.objects.filter(pass_date__month =12)
    studentobj = Student.objects.filter(pass_date__month__gt =1)# two condition applying after lookup also
    studentobj = Student.objects.filter(pass_date__day =2)
    studentobj = Student.objects.filter(pass_date__day__gt =2)
    studentobj = Student.objects.filter(pass_date__week =12)
    studentobj = Student.objects.filter(pass_date__week__gt =12)
    studentobj = Student.objects.filter(pass_date__week_day =1 )
    studentobj = Student.objects.filter(pass_date__quater=2 )
    studentobj = Student.objects.filter(pass_date__time__gt=time(21,17) )
    studentobj = Student.objects.filter(pass_date_time__hour__gt=2 )
    studentobj = Student.objects.filter(pass_date_time__minute__gt=2 )
    studentobj = Student.objects.filter(pass_date_time__secound__gt=2 )
    studentobj = Student.objects.filter(roll__isnull=False )

    #Aggregation
    studentobj = Student.objects.all()
    average = studentobj.aggregate(Avg("marks"))
    sum = studentobj.aggregate(Sum("marks"))
    minimun = studentobj.aggregate(Min("marks"))
    maximum = studentobj.aggregate(Max("marks"))
    count = studentobj.aggregate(Count("marks"))


    # print(type(studentobj))
    context = { "student"  : studentobj,"students"  : studentobj}

    return render(request,"modelchecking/home.html",context)