
from django.urls import path
from .views import home,checknew


urlpatterns = [
    path('' , home , name="home"),
    path("checknew/" ,checknew , name="checknew")

]