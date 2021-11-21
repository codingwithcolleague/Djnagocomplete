from django import forms
from django.forms import fields, models
from .models import User

class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = ['username','password','email' ]
        fields = "__all__"
        exclude = ("email",)


class UserForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)


    def clean_username(self):
        username = self.cleaned_data.get("username")
        print(username)
        if username == "rahul":
            raise forms.ValidationError("Please enter another username")

    def clean(self):
        clean_data =  super().clean()
        if clean_data.get("username") == "Raj":
            raise forms.ValidationError("Please enter the different name")
        return clean_data