from django.urls import path
from .views import TeacherRegistrationView, SearchStudentsView, teacher_login


urlpatterns = [
    path('register/teacher/', TeacherRegistrationView.as_view(), name='register_teacher'),
    path('search/', SearchStudentsView.as_view(), name='search_students'),
    path('login/', teacher_login, name='teacher_login'),
]
