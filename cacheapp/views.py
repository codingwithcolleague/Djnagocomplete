from django.shortcuts import render
from django.views.decorators.cache import cache_page

# Create your views here.
@cache_page(20)
def home(request):
    return render(request,"cacheapp/home.html")


def contact(request):
    return render(request,"cacheapp/home.html")

def check(request):
    return render(request,"cacheapp/check.html")