from django.contrib import admin
from .models import Student, Teacher, ClassRoom, School

@admin.register(Student)
class StundentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'birthday', 'gender', 'email')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('username', 'subject', 'clas', 'phone')

@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')


admin.site.register(School)