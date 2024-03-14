from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.db import connection
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import TeacherRegistrationForm, TeacherLoginForm
from .models import Student, Teacher
from django.db.models import Q


class TeacherRegistrationView(View):
    def get(self, request):
        form = TeacherRegistrationForm()
        return render(request, 'users/register_teacher.html', {'form': form})

    def post(self, request):
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Вы успешно зарегистрировались.<br>"
                                "<a href='/students/home/'>Вернуться на главную страницу</a><br>"
                                "<a href='/users/login/'>Войти в личный кабинет</a>")
        return render(request, 'users/register_teacher.html', {'form': form})


class TeacherLoginView(View):
    def get(self, request):
        form = TeacherLoginForm()
        return render(request, 'users/teacher_login.html', {'form': form})

    def post(self, request):
        form = TeacherLoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            try:
                teacher = Teacher.objects.get(phone=phone)
                if check_password(password, teacher.password):
                    login(request, teacher)
                    return redirect('/students/home/')
                else:
                    form.add_error(None, 'Неверный пароль.')
            except Teacher.DoesNotExist:
                form.add_error(None, 'Пользователя с таким номером не существует.')
        return render(request, 'users/teacher_login.html', {'form': form})

class SearchStudentsView(View):
    def get(self, request):
        query = request.GET.get('query', '')
        students = None
        if query:
            q_objects = Q()
            for term in query.split():
                q_objects &= (Q(name__icontains=term) | Q(surname__icontains=term))

            students = Student.objects.filter(q_objects)
        return render(request, 'users/search_students.html', {'students': students, 'query': query})


# user = authenticate(request, phone=phone, password=password)