from django import forms
from django.db import models
from django.db.models import fields

from classbasedvieww.models import Student

class ContactForm(forms.Form):
    name = forms.CharField(max_length=200)


from django import forms

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        