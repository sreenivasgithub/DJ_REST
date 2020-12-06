from django.db import models

class CourseModel(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.course

class StudentModel(models.Model):
    Stdid = models.AutoField(primary_key=True)
    Stdname = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    course_id = models.ForeignKey(CourseModel, on_delete=models.CASCADE, null=True)
    class Meta:
        db_table = "studenttable"

class AttendanceModel(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(StudentModel, on_delete=models.CASCADE, default=True)
    Attendance = models.CharField(max_length=100)

class AssignmentModel(models.Model):
    status_report = (
        ('Completed', 'Completed'),
        ('Pending', 'Pending')
    )
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(StudentModel, on_delete=models.CASCADE, default=True)
    Assignment = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=status_report)



