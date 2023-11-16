
from django.urls import path
from mainapp import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login', views.login_page, name='login_page'),
    path('add_course', views.AddCourse.as_view(), name='add_course'),
    #path('update_course/<int:id>', views.update_course, name='update_course'),
    path('course_detail/<int:id>', views.CourseDetailView.as_view(), name='course_detail'),
    path('courses', views.Courses.as_view(), name='courses'),
    path('students', views.Students.as_view(), name='students'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('enroll', views.EnrollStudent.as_view(), name='enroll'),
    path('add_trainer', views.AddTrainer.as_view(), name='add_trainer'),
    path('trainers', views.Trainers.as_view(), name='trainers'),
    path('add-contact-info', views.add_contact_info, name='add_info'),
    #path('delete-record/<int:id>', views.delete_record, name='delete-record'),
    path('register', views.register_page, name='register_page'),
]