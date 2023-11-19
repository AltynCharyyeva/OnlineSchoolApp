
from django.urls import path
from mainapp import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login', views.login_page, name='login_page'),
    path('logout', views.logout_page, name='logout'),
    path('add_course', views.AddCourse.as_view(), name='add_course'),
    path('course_detail/<int:id>', views.CourseDetailView.as_view(), name='course_detail'),
    path('student_detail/<int:id>', views.StudentDetailView.as_view(), name='student_detail'),
    path('courses', views.Courses.as_view(), name='courses'),
    path('students', views.Students.as_view(), name='students'),
    path('users', views.Users.as_view(), name='users'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('enroll', views.EnrollStudent.as_view(), name='enroll'),
    path('add_trainer', views.AddTrainer.as_view(), name='add_trainer'),
    path('trainers', views.Trainers.as_view(), name='trainers'),
    path('add-contact-info', views.add_contact_info, name='add_info'),
    path('register', views.register_page, name='register_page'),
    path('access-forbidden', views.access_forbidden_page, name='forbidden'),
    path('success_sign_up', views.success_sign_in, name='success'),
    path('enroll_success', views.enroll_success, name='enroll_success')
    #path('delete-record/<int:id>', views.delete_record, name='delete-record'),
    #path('update_course/<int:id>', views.update_course, name='update_course'), 
]