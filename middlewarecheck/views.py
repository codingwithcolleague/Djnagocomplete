from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

# Create your views here.
def home(request):
    if 2 % 0 == 0:
        print("yes")
    return HttpResponse("Hello")


def checknew(request):
    context = {"name" :"Rahul"}
    return TemplateResponse(request,"middlewarecheck/home.html",context)