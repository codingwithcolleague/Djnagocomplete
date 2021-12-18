
from django.urls import path
from .views import (home,MyClass,MyLoveClass,ContactClass,HomeTemplateView,
            contactFunction,newsLife,NewsClass)

urlpatterns = [
    path('' , home , name="home"),
    path('myclass/' , MyClass.as_view() , name="myclass"),
    path('loveclass/' , MyLoveClass.as_view() , name="loveclass"),
    path('contactfun/' , contactFunction , name="contactfunction"),
    path('contact/' , ContactClass.as_view() , name="contact"),
    path('news/' , newsLife , { "template_name" : "classbasedvieww/news.html" } , name="news"),
    path('newsClass/' , NewsClass.as_view() , name="newsclass"),
    path('templateview/' , HomeTemplateView.as_view() , name="templateview")


]