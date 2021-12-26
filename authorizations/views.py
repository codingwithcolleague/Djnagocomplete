from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
# Create your views here.

@login_required
def myprofile(request):
    return HttpResponse("My Profile")

@staff_member_required
def myhome(request):
    return HttpResponse("My Home")

class Mycheck(TemplateView):
    template_name = "authorizations/home.html"


class AbooutTemplate(TemplateView):
    template_name = "authorizations/home.html"

    @method_decorator(login_required)
    def dispatch(self,*args,**kwargs):
        return super().dispatch(*args,**kwargs)