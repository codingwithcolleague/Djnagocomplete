
from django.conf.urls import url
from django.urls import path
from django.views.generic.base import RedirectView

from classbasedvieww.form import ContactForm
from .views import (home,MyClass,MyLoveClass,ContactClass,HomeTemplateView,
            contactFunction,newsLife,NewsClass,
            
        StudentListView,StudentDeatilsView,ContractFormView,thankyou,StudentCreateView,
        StudentFormCreateView,StudentFormUpdateView,StudentDeleteView
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



    path('studentlist/' , StudentListView.as_view() , name="studentlist"),
    path('studentdetails/<int:pk>' , StudentDeatilsView.as_view() , name="studentdetails"),
    path('contactview/' , ContractFormView.as_view() , name="contactview"),
    path('thankyou/' , thankyou , name="thankyou"),
    path('studentcreate/' , StudentCreateView.as_view() , name="studentcreate"),
    path('studentformcreate/' , StudentFormCreateView.as_view() , name="studentformcreate"),
    path('studentformupdate/<int:pk>' , StudentFormUpdateView.as_view() , name="studentformupdate"),
    path('studentdelete/<int:pk>' , StudentDeleteView.as_view() , name="studentdelete")


]