from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Teacher

class TeacherRegistrationForm(UserCreationForm):
    phone = forms.CharField(label='Номер телефона')
    class_number = forms.CharField(label='Класс')
    subject = forms.CharField(label='Предмет')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)

    class Meta:
        model = Teacher
        fields = ['phone', 'class_number', 'subject', 'password1', 'password2']


class TeacherLoginForm(forms.Form):
    phone = forms.CharField(label='Номер телефона')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
