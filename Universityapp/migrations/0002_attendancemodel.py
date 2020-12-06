# Generated by Django 3.1.3 on 2020-11-23 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Universityapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Attendance', models.CharField(max_length=4)),
                ('Stdname', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Universityapp.studentmodel')),
            ],
        ),
    ]
