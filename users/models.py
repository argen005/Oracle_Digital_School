from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from school import settings


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

@receiver(post_save, sender=Student)
def send_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Добро пожаловать!'
        message = f'Дорогой {instance.name},\n\nДобро пожаловать в нашу школу!'
        from_email = settings.EMAIL_HOST_USER
        to_email = [instance.email]
        send_mail(subject, message, from_email, to_email)


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

