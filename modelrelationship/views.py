from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from .models import Page, Song, Post

def home(request):
    return render(request,"modelrelationship/home.html")

def show_user_data(request):
    data1 = User.objects.all()
    data2 = User.objects.filter(email='rahul@gmail.com')
    data3 = User.objects.filter(page__page_cat='Programming')
    data4 = User.objects.filter(post__post_publish_date='2021-12-11')
    data5 = User.objects.filter(song__song_duration=3)
    return render(request,"modelrelationship/user.html",{"data1" : data1,"data2" : data2, "data3" : data3 , "data4" : data4 , "data5" : data5 })


def show_page_data(request):
    data1 = Page.objects.all()
    data2 = Page.objects.filter(page_cat='Programming')
    data3 = Page.objects.filter(user__email='rahul@gmail.com')
    return render(request,"modelrelationship/page.html",{"data1" : data1,"data2" : data2, 
    "data3" : data3 })
