
from django.urls import path,register_converter
from .views import home,profile
from .converter import FourDigitYearConverter
register_converter(FourDigitYearConverter,'yyyy')


urlpatterns = [
    path('' , home , name="home"),
    path("myprofile/<int:id>" , profile , name="profile"),
    path("session/<yyyy:id>/" , profile , name="session")

]