from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Teacher

class TeacherRegistrationForm(UserCreationForm):
    phone = forms.CharField(label='Номер телефона')
    clas = forms.CharField(label='Класс')
    subject = forms.CharField(label='Предмет')

    class Meta:
        model = Teacher
        fields = ['username', 'phone', 'clas', 'subject', 'password1', 'password2']

from django import forms
from .models import Teacher

class TeacherAuthenticationForm(forms.Form):
    identifier = forms.CharField(label='Имя пользователя или номер телефона')
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_identifier(self):
        identifier = self.cleaned_data['identifier']
        if not identifier:
            raise forms.ValidationError('Введите имя пользователя или номер телефона')
        return identifier

    def clean(self):
        cleaned_data = super().clean()
        identifier = cleaned_data.get('identifier')
        password = cleaned_data.get('password')
        if identifier and password:
            try:
                teacher = Teacher.objects.get(Q(username=identifier) | Q(phone_number=identifier))
            except Teacher.DoesNotExist:
                raise forms.ValidationError('Пользователь с таким именем пользователя или номером телефона не найден')
            if not teacher.check_password(password):
                raise forms.ValidationError('Неверный пароль')
        return cleaned_data