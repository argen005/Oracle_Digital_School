from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import TeacherRegistrationForm, TeacherAuthenticationForm
from .models import Student
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
            return HttpResponse('Teacher registration successful.')
        return render(request, 'users/register_teacher.html', {'form': form})


def search_students(request):
    query = request.GET.get('query', '')
    students = None
    if query:
        q_objects = Q()
        for term in query.split():
            q_objects &= (Q(name__icontains=term) | Q(surname__icontains=term))

        students = Student.objects.filter(q_objects)
    return render(request, 'users/search_students.html', {'students': students, 'query': query})

def teacher_login(request):
    if request.method == 'POST':
        form = TeacherAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('Аутентификация прошла успешно')
                # return redirect('home')
    else:
        form = TeacherAuthenticationForm()
    return render(request, 'users/teacher_login.html', {'form': form})