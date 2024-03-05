from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.views import View
from users.models import Student
from .forms import StudentForm

class StudentListView(View):
    def get(self, request):
        students = Student.objects.all()
        return render(request, 'students/student_list.html', {'students': students})

class StudentDetailView(View):
    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        return render(request, 'students/student_detail.html', {'student': student})

class StudentCreateView(View):
    def get(self, request):
        form = StudentForm()
        return render(request, 'students/student_form.html', {'form': form})

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student = form.save()
            #
            # subject = 'Добро пожаловать!'
            # message = f'Дорогой {new_student.name},\n\nДобро пожаловать в нашу школу!'
            # from_email = settings.EMAIL_HOST_USER
            # to_email = [new_student.email]
            # send_mail(subject, message, from_email, to_email)

            return HttpResponse('Студент успешно создан')
        return render(request, 'students/student_form.html', {'form': form})

class StudentUpdateView(View):
    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        form = StudentForm(instance=student)
        return render(request, 'students/student_form.html', {'form': form})

    def post(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        return render(request, 'students/student_form.html', {'form': form})

class StudentDeleteView(View):
    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        return render(request, 'students/student_confirm_delete.html', {'student': student})

    def post(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return HttpResponse("Студент успешно удален. "
                            "<a href='/students/home/'>Вернуться на главную страницу</a>")


def home(request):
    return render(request, 'students/home.html')
