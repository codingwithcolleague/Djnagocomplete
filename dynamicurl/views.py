from django.shortcuts import render


# Create your views here.
def home(request):
    context = {}
    return render(request,"dynamic.html",context)


# Create your views here.
def profile(request,id):
    context = {"id" : id }
    return render(request,"dynamic/profile.html",context)