
from django.urls import path
from .views import home,contact,check
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('' , home , name="home"),
    path("contact/" , cache_page(20)(contact)),
    path('check/' , check , name="check"),


]