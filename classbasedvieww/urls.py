
from django.conf.urls import url
from django.urls import path
from django.views.generic.base import RedirectView
from .views import (home,MyClass,MyLoveClass,ContactClass,HomeTemplateView,
            contactFunction,newsLife,NewsClass,
            
        StudentListView
    )

urlpatterns = [
    path('' , home , name="home"),
    path('myclass/' , MyClass.as_view() , name="myclass"),
    path('loveclass/' , MyLoveClass.as_view() , name="loveclass"),
    path('contactfun/' , contactFunction , name="contactfunction"),
    path('contact/' , ContactClass.as_view() , name="contact"),
    path('news/' , newsLife , { "template_name" : "classbasedvieww/news.html" } , name="news"),
    path('newsClass/' , NewsClass.as_view() , name="newsclass"),
    path('templateview/' , HomeTemplateView.as_view() , name="templateview"),
    path('redirectview/' , RedirectView.as_view(url="/classbasedvieww") , name="templateview"),



    path('studentlist/' , StudentListView.as_view() , name="studentlist")

]