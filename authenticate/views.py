from django.http.response import HttpResponse
from django.shortcuts import render
from .form import Registration,SignUpForm
from django.contrib.auth.forms import AuthenticationForm,SetPasswordForm,PasswordChangeForm
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
# Create your views here.

def userRegistration(request):
    if request.method == "POST":
        fm = Registration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data.get("name")
            age = fm.cleaned_data.get("age")
            mobile = fm.cleaned_data.get("mobile")
            print(fm.cleaned_data)
            # insert = Student.objects.create(name=name, age=age,mobile=mobile)
            # return HttpResponse("Inserted Succesfully")

        return render(request,"authenticate/userregistration.html", {"fm":fm})
    else:
        fm = Registration()
    return render(request,"authenticate/userregistration.html", {"fm":fm})


def userRegistrationModelView(request):
    form = SignUpForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password1 = form.cleaned_data.get("password1")
            password2 = form.cleaned_data.get("password2")
            print(username,password1,password2)
            form.save()
            return HttpResponse("You have succefully submitted")

        return render(request,"authenticate/userregistration.html",{"form" : form})
    else:
        return render(request,"authenticate/userregistration.html",{"form" : form})


def userlogin(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponse("Login Succesfully")
        return render(request,"authenticate/userregistration.html",{"form" : form})
    else:
        if request.user.is_authenticated:
            return HttpResponse("Already Login")
        form = AuthenticationForm()
        return render(request,"authenticate/userregistration.html",{"form" : form})


def userlogout(request):
    logout(request)
    return HttpResponse("Logout Succesfully")



def changeUserPassword(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                return HttpResponse("Password Reset Successfully")
            return render(request,"userregistration.html",{"form":fm})
        else:
            fm = PasswordChangeForm(user=request.user)
            return render(request,"userregistration.html",{"form":fm})
    else:
        return HttpResponse("Password Try To Login")



def changeUserPasswordWithoutold(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = SetPasswordForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                return HttpResponse("Password Reset Successfully")
            return render(request,"userregistration.html",{"form":fm})
        else:
            fm = SetPasswordForm(user=request.user)
            return render(request,"userregistration.html",{"form":fm})
    else:
        return HttpResponse("Password Try To Login")
