from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from mainapp import models



class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    
class TrainerForm(forms.ModelForm):
    class Meta:
        model = models.Trainer
        exclude = ['create_date', 'modify_date']


class CourseForm(forms.ModelForm):
    class Meta:
        model = models.Course
        exclude = ['create_date', 'modify_date', 'course_logo']

class StudentForm(forms.ModelForm):
    class Meta: 
        model = models.Student
        exclude = ['create_date', 'modify_date', 'trainers']


    