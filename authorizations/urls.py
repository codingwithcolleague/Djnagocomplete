from django.urls import path,include
from .views import myprofile,Mycheck
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("profile/" ,  myprofile ),
    path("home/" ,  login_required(Mycheck.as_view()) )

]