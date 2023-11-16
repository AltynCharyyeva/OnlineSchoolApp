from django.contrib import admin
from mainapp import models

# Register your models here.
admin.site.register(models.Trainer)
admin.site.register(models.Student)
admin.site.register(models.Course)
admin.site.register(models.School_info)
#admin.site.register(models.Enrollment)