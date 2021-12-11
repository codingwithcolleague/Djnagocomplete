
from django.urls import path
from .views import home,show_user_data,show_page_data

urlpatterns = [
    path('' , home , name="home"),
    path('show_user_data/' , show_user_data , name="show_user_data"),
    path("show_page_data/" , show_page_data , name="show_page_data")

]