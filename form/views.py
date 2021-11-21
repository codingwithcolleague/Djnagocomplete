from django.http.response import HttpResponse
from django.shortcuts import render
from .form import UserModelForm,UserForm
from .models import User

# Create your views here.
def insertuser(request):
    form = UserModelForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            # print("formm", form.cleaned_data.get)
            form.save()
            return HttpResponse("Userser Inserted Successfully")
    else:
        context = { "form"  : form}
    return render(request,"form/createuser.html",context)

def insertuserForm(request):
    form = UserForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username =  form.cleaned_data.get("username")
            password =  form.cleaned_data.get("password")
            email =  form.cleaned_data.get("email")
            print(username,password,email)
            # obj = User.objects.create(username=username,password=password,email=email)
            # if obj:
            #     return HttpResponse("Userser Inserted Successfully")
            context = { "form"  : form}
            return render(request,"form/createuser.html",context)
    context = { "form"  : form}
    return render(request,"form/createuser.html",context)