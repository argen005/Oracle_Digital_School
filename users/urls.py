from django.urls import path
from .views import TeacherRegistrationView, SearchStudentsView, TeacherLoginView


urlpatterns = [
    path('register/teacher/', TeacherRegistrationView.as_view(), name='register_teacher'),
    path('search/', SearchStudentsView.as_view(), name='search_students'),
    path('login/', TeacherLoginView.as_view(), name='teacher_login'),
]
