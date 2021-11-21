
from django.urls import path,register_converter
from .views import insertuser,insertuserForm


urlpatterns = [
    path('' , insertuser , name="create"),
    path('createform/' , insertuserForm , name="createusingform")
]