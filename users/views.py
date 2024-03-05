from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import TeacherRegistrationForm, TeacherAuthenticationForm
from .models import Student, Teacher
from django.db.models import Q
from django.contrib.auth import authenticate, login


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



class TeacherLoginView(View):
    def get(self, request):
        form = TeacherAuthenticationForm()
        return render(request, 'users/teacher_login.html', {'form': form})

    def post(self, request):
        form = TeacherAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            try:
                teacher = Teacher.objects.get(username=username)
            except Teacher.DoesNotExist:
                return HttpResponse('Такого пользователя не существует')
            password = form.cleaned_data.get('password')
            if teacher.check_password(password):
                return HttpResponse('Вы вошли в систему')
        return HttpResponse('Неверный логин или пароль')

# class TeacherLogin(TemplateView):
#     template_name = 'users/teacher_login.html'
#     form_class = TeacherAuthenticationForm
#
#     def get_context_data(self, **kwargs):
#         form = self.form_class
#         return {'form': form}
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
