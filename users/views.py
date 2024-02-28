from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import TeacherRegistrationForm

from django.shortcuts import redirect

def register_teacher(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(f'Teacher registration successful.)')
    else:
        form = TeacherRegistrationForm()

    return render(request, 'users/register_teacher.html', {'form': form})
