from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Teacher

class TeacherRegistrationForm(UserCreationForm):
    phone = forms.CharField(label='Номер телефона')
    clas = forms.CharField(label='Класс')
    subject = forms.CharField(label='Предмет')

    class Meta:
        model = Teacher
        fields = ['username', 'phone', 'clas', 'subject', 'password1', 'password2']
