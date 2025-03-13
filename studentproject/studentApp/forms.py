from django import forms
from django.core import validators

def start_with_d(value):
    if value[0].lower() != 'd':
        raise forms.ValidationError("Name should be start with D|d")

class StudentForm(forms.Form):
    name=forms.CharField(validators=[validators.MinLengthValidator(4),validators.MaxLengthValidator(8)])
    name=forms.CharField(validators=[start_with_d])
    marks=forms.IntegerField()