from django.contrib.auth.models import AbstractUser
from django.db import models

class Student(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=50)
    surname = models.CharField(verbose_name='Фамилия', max_length=50)
    fathername = models.CharField(verbose_name='Отчество', max_length=50, blank=True, null=True)
    email = models.EmailField(verbose_name='Email', unique=True, null=True, blank=True)
    birthday = models.DateField(verbose_name='Дата рождения')
    adress = models.CharField(verbose_name='Адрес', max_length=200)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('Ж', 'Female')])
    photo = models.ImageField(verbose_name='Фото', upload_to='photos/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

class Teacher(AbstractUser):
    phone = models.CharField(verbose_name='Номер телефона', max_length=20, unique=True)
    clas = models.CharField(verbose_name='Класс', max_length=10)
    groups = models.ManyToManyField('auth.Group', related_name='teachers_groups')
    subject = models.CharField(verbose_name='Предмет', max_length=50)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'


class ClassRoom(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.OneToOneField('Teacher', on_delete=models.CASCADE, related_name='ClassRoom')
    students = models.ManyToManyField('Student', related_name='classes')

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'

class School(models.Model):
    name = models.CharField(max_length=100)
    classes = models.ManyToManyField('ClassRoom', related_name='schools')

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'

