from datetime import datetime, timedelta
from django.shortcuts import render

# Create your views 

def createcookie(request):
    response =  render(request,"cookiesession/createcookie.html")
    # response.set_cookie("name" , "rahul")
    response.set_cookie("name" , "rahul" , expires=datetime.utcnow()+timedelta(days=1))
    return response

def getcookie(request):
    name = request.COOKIES.get("name")
    print(name)
    return render(request,"cookiesession/createcookie.html" , {"name" : name})

def deleteCookie(request):
    # del request.COOKIES["name"]
    d = request.COOKIES.get("name")
    myy =  render(request,"cookiesession/createcookie.html")
    myy.delete_cookie("name")
    d = request.COOKIES.get("name")
    print(d)
    return myy

def createSession(request):
    request.session["name"] = "Rahul"
    return render(request,"cookiesession/createcookie.html" , {"session" : "yes"})

def getSession(request):
    name = request.session["name"]
    # request.session.get("name")
    # request.session.keys()
    # request.session.items()
    # request.session.setdefault("age",24)
    return render(request,"cookiesession/createcookie.html" , {"session" : name})

def delSession(request):
    del request.session["name"]
    return render(request,"cookiesession/createcookie.html" , {"session" : "yes"})
