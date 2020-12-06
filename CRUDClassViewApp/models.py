from django.db import models

class EmployeeModel(models.Model):
    Empid = models.IntegerField(primary_key=True)
    Empname = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    salary = models.IntegerField()
    class Meta:
        db_table = "employeetable"
