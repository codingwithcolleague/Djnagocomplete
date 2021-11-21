from django import forms
from django.contrib.auth import models
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Registration(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    mobile = forms.CharField(max_length=200)
    
    def clean_age(self):
        age = self.cleaned_data.get("age")
        if age < 15:
            raise ValidationError("Please insert other age")
        return age

    def clean(self):
        clean_data =  super().clean()
        if clean_data.get("name") == "Raj":
            raise ValidationError("Please enter the different name")
        return clean_data


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email","first_name","last_name"]