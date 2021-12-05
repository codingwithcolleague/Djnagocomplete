from django.shortcuts import render,HttpResponse
from signaltask import customsignal
# Create your views here.

def homee(request):
    print("customeeeeee")
    customsignal.notification.send(sender=None,request=request,user=["geeky","show"])
    return HttpResponse("This is return")