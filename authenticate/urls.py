
from django.urls import path,register_converter
from .views import userRegistrationModelView,userlogin,userlogout

urlpatterns = [
    path('' , userRegistrationModelView , name="userregistration"),
    path("userlogin/",  userlogin, name="userlogin"),
    path("userlogout/",  userlogout, name="userlogout")

]