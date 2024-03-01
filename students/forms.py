from django import forms
from users.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'email', 'birthday', 'adress', 'gender', 'photo']