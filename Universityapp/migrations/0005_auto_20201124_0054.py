# Generated by Django 3.1.3 on 2020-11-23 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Universityapp', '0004_auto_20201124_0024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendancemodel',
            name='Stdname',
        ),
        migrations.AddField(
            model_name='attendancemodel',
            name='student_id',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Universityapp.studentmodel'),
        ),
        migrations.AlterField(
            model_name='attendancemodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
