from typing import Any
from django.http import HttpResponse
from django.shortcuts import render, redirect
from mainapp import models, forms
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User


# Create your views here.

def homepage(request):
    return render(request, 'mainapp/home.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('success')
        else:
            messages.success(request, ("There was an error logging in"))
            return redirect('login_page')
    return render(request, 'mainapp/login.html')


def logout_page(request):
    logout(request)
    messages.success(request, ("Loogged out succesfull"))
    return redirect('homepage')

    

def register_page(request):
    if request.method != 'POST':
        form = forms.CustomUserForm()
    else:
        form = forms.CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')

    context = {'form': form}

    return render(request, 'mainapp/register.html', context)

def success_sign_in(request):
    return render(request, 'mainapp/success.html')


class EnrollStudent(LoginRequiredMixin, CreateView):
    login_url = "login_page"
    form_class = forms.StudentForm
    template_name = 'mainapp/enroll.html'
    success_url = 'enroll_success'

    
    def form_valid(self, form):
        # Get the selected courses from the form data
        selected_courses = form.cleaned_data['course']
        

        response = super().form_valid(form)

        # Iterate over selected courses and add the trainers for each course to the student
        for course in selected_courses:
            c = models.Course.objects.get(course_name=course.course_name)
            form.instance.trainers.add(c.trainer)

        # Call the super method to save the form and perform the default behavior
        return response


def enroll_success(request):
    return render(request, 'mainapp/enrollsuccess.html')

class StudentDetailView(LoginRequiredMixin, DetailView):
    login_url = "login_page"
    model = models.Student
    template_name = 'mainapp/student_detail.html'
    context_object_name = 'student'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs: Any):
        context =  super().get_context_data(**kwargs)
        return context



class Trainers(ListView):
    model = models.Trainer
    template_name = 'mainapp/trainers.html'
    context_object_name = 'trainers'


class Courses(ListView):
    model = models.Course
    template_name = 'mainapp/courses.html'
    context_object_name = 'courses'


def access_forbidden_page(request):
    return render(request, 'mainapp/forbidden.html')



class Students(UserPassesTestMixin, ListView):
    model = models.Student
    template_name = 'mainapp/students.html'
    context_object_name = 'students'

    def test_func(self):
        return self.request.user.username.startswith('altyn')

    def handle_no_permission(self):
        return render(
            self.request,
            'mainapp/forbidden.html',
            {'redirect_url': 'forbidden'}
        )

    def get_login_url(self) -> str:
        return ('forbidden')


class Users(UserPassesTestMixin, ListView):
    model = User
    template_name = 'mainapp/users.html'
    context_object_name = 'users'

    def test_func(self):
        return self.request.user.username.startswith('altyn')

    def handle_no_permission(self):
        return render(
            self.request,
            'mainapp/forbidden.html',
            {'redirect_url': 'forbidden'}
        )

    def get_login_url(self) -> str:
        return ('forbidden')



@login_required
def add_contact_info(request):
    models.School_info.objects.create(
        school_name = 'ITSchool',
        email = 'office@itschool.ro',
        address = 'Blv.General Ion Dragolina, Nr. 27, Timisoara, Romania',
        tel = '+40 737 880 420'
    )

    return redirect('homepage')


class Contact(ListView):
    model = models.School_info
    template_name = 'mainapp/contact.html'
    context_object_name = 'school_info'
    
    
    
class AddTrainer(UserPassesTestMixin, CreateView):
    form_class = forms.TrainerForm
    template_name = 'mainapp/add_trainer.html'
    success_url = 'trainers'
    model = models.Trainer

    def test_func(self):
        return self.request.user.username.startswith('altyn')

    def handle_no_permission(self):
        return render(
            self.request,
            'mainapp/forbidden.html',
            {'redirect_url': 'forbidden'}
        )

    def get_login_url(self) -> str:
        return ('forbidden')


class AddCourse(UserPassesTestMixin, CreateView):
    form_class = forms.CourseForm
    template_name = 'mainapp/add_course.html'
    success_url = 'courses'
    model = models.Course

    def test_func(self):
        return self.request.user.username.startswith('altyn')

    def handle_no_permission(self):
        return render(
            self.request,
            'mainapp/forbidden.html',
            {'redirect_url': 'forbidden'}
        )

    def get_login_url(self) -> str:
        return ('forbidden')


class CourseDetailView(DetailView):
    model = models.Course
    template_name = 'mainapp/course_detail.html'
    context_object_name = 'course'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs: Any):
        context =  super().get_context_data(**kwargs)
        return context



# def delete_record(request, id):
#     instance = models.School_info.objects.get(id=id)
#     instance.delete()
#     return redirect('homepage')


# def update_course(request, id):
#     course = models.Course.objects.get(id=id)
#     course.description = ('absdefg')
#     course.save()
#     return HttpResponse('Success')
