"""alltopicdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from signaltask.views import homee

urlpatterns = [
    path('admin/', admin.site.urls),
    path("dynamicurl/" , include(("dynamicurl.urls" , "dynamicurl") , namespace="dynamicurl")),
    path("form/" , include(("form.urls" , "form") , namespace="form")),
    path("authenticate/" , include(("authenticate.urls" , "authenticate") , namespace="authenticate")),
    path("cookiesession/" , include(("cookiesession.urls" , "cookiesession") , namespace="cookiesession")),
    path("cacheapp/" , include(("cacheapp.urls" , "cacheapp") , namespace="cacheapp")),
    path("customesignal/" , homee ),
    path("middlewarecheck/" , include(("middlewarecheck.urls" , "middlewarecheck") , namespace="middlewarecheck")),
    path("modelchecking/" , include(("modelchecking.urls" , "modelchecking") , namespace="modelchecking")),
    path("modelmanagerconcept/" , include(("modelmanagerconcept.urls" , "modelmanagerconcept") , namespace="modelmanagerconcept")),
    path("modelrelationship/" , include(("modelrelationship.urls" , "modelrelationship") , namespace="modelrelationship")),
    path("classbasedvieww/" , include(("classbasedvieww.urls" , "classbasedvieww") , namespace="classbasedvieww")),
    path("authorizations/" , include(("authorizations.urls" , "authorizations") , namespace="authorizations")),
    path('accounts/' , include('django.contrib.auth.urls')),
    path('accounts/' , include(("authorizations.urls" , "authorizations") , namespace="authorizations"))

]

