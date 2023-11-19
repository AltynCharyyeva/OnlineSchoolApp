from django.db import models

# Create your models here.

class Trainer(models.Model):
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    addres=models.CharField(max_length=200)
    email=models.EmailField()
    tel=models.CharField(max_length=40)
    about=models.TextField()
    profession=models.CharField(max_length=30)
    create_date=models.DateTimeField(auto_now_add=True)
    modify_date=models.DateTimeField(auto_now=True)

    class Meta:
        db_table='trainer'

    def __str__(self) -> str:
        return f'{self.name} {self.surname} {self.profession}'
    
class Course(models.Model):
    course_name=models.CharField(max_length=100)
    description=models.TextField()
    cost=models.CharField(max_length=10)
    start_time=models.DateTimeField()
    orar=models.CharField(max_length=50)
    trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE, blank=True, null=True)
    course_logo=models.CharField(max_length=500, null=True)
    create_date=models.DateTimeField(auto_now_add=True)
    modify_date=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.course_name}'
    
    class Meta:
        db_table = 'course'



class Student(models.Model):
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    addres=models.CharField(max_length=200)
    email=models.EmailField()
    tel=models.CharField(max_length=40)
    trainers=models.ManyToManyField(Trainer, blank=True)
    course=models.ManyToManyField(Course, blank=True)
    create_date=models.DateTimeField(auto_now_add=True)
    modify_date=models.DateTimeField(auto_now=True)


    class Meta:
        db_table='student'

    def __str__(self) -> str:
        return f'Name: {self.name} Surname: {self.surname}'


class School_info(models.Model):
    school_name=models.CharField(max_length=40)
    email=models.EmailField()
    address=models.CharField(max_length=200)
    tel=models.CharField(max_length=50)

    class Meta:
        db_table = 'school_info'

# class Enrollment(models.Model):
#     student=models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
#     course=models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
#     enrollment_date=models.DateField()
    
