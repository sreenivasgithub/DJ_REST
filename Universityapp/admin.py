from django.contrib import admin
from .models import StudentModel, CourseModel, AttendanceModel, AssignmentModel

# Register your models here.

admin.site.register(StudentModel)
admin.site.register(CourseModel)
admin.site.register(AttendanceModel)
admin.site.register(AssignmentModel)