from django.shortcuts import render
from django.views.decorators import cache
from django.views.decorators.cache import cache_page
from django.core.cache import cache

# Create your views here.
@cache_page(20)
def home(request):
    return render(request,"cacheapp/home.html")


def contact(request):
    return render(request,"cacheapp/home.html")

def check(request):
    return render(request,"cacheapp/check.html")

def lowlevel(request):
    # mv = cache.get("movie", "has_expire")
    # if mv == "has_expire":
    #     cache.set("movie", "Rahul is Say On", 5)
    #     mv = cache.get("movie")
    # print("ss",mv)
    # mv = cache.get_or_set("age",4747,10)
    data = { "name":"Rahul" , "rol":10}
    # mv = cache.set_many(data,30)
    mv = cache.get_many(data)
    return render(request,"cacheapp/check.html", {"mvall" : mv})