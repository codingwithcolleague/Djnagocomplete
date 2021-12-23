from django.db import models
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from .form import ContactForm
from django.views.generic import ListView
from .models import Student

# Create your views here.
def home(request):
    return HttpResponse('<h1> Function Based View </h1>')
    # return render(request,"classbasedvieww/home.html")

class MyClass(View):
    name = "Rahul"
    def get(self,request):
        return HttpResponse('<h1> Class Based View </h1>' + self.name)

class MyLoveClass(View):
    def get(self,request):
        context = {"love" : "My Love"}
        return render(request,"classbasedvieww/home.html",context)


def contactFunction(request):
    forms = ContactForm(request.POST or None)
    if request.method == "POST":
        if forms.is_valid():
            name  = forms.cleaned_data.get("name")
            return HttpResponse(name)
    context = {"form" : forms}
    return render(request,"classbasedvieww/contact.html",context)

class ContactClass(View):
    def get(self,request):
        forms = ContactForm()
        context = {"form" : forms}
        return render(request,"classbasedvieww/contact.html",context)

    def post(self,request):
        forms = ContactForm(request.POST)
        print( "formmmmmmm" , forms)
        if forms.is_valid():
            name =forms.cleaned_data.get("name")
            return HttpResponse(name)


def newsLife(request,template_name):
    context = {"content" : "Hi Siri"} 
    return render(request,template_name ,context)


class NewsClass(View):
    template_name = "classbasedvieww/contact.html"
    def get(self,request):
        context = {"content" : "Hi Siri"} 
        return render(request, self.template_name,context)

class HomeTemplateView(TemplateView):
    template_name = "classbasedvieww/news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Rahul"
        return context
    

#Generic Class Based View

class StudentListView(ListView):
    model = Student
    template_name = "classbasedvieww/student_list.html"
    context_object_name = "students"

    def get_queryset(self):
        return Student.objects.filter(name__startswith="R")

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context["fresher"] = Student.objects.all().order_by("name")
        return context

    def get_template_names(self):
        if self.request.COOKIES.get("users") == "sonam":
            template_name = "classbasedvieww/sonam.html"
        else:
            template_name = self.template_name
        return [template_name]