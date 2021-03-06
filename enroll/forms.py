from django import forms
from django.forms import widgets
from .models import Student

class StudentRegister(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "email", "password"]
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }