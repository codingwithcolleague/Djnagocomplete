
from django.urls import path
from .views import createcookie,getcookie,deleteCookie,createSession,getSession,delSession

urlpatterns = [
    path('' , createcookie , name="createcookie"),
    path('getcookie/' , getcookie , name="getcookie"),
    path('deleteCookie/' , deleteCookie , name="deleteCookie"),
    path('createSession/' , createSession , name="createSession"),
    path('getSession/' , getSession , name="getSession"),
    path('delSession/' , delSession , name="delSession"),


]