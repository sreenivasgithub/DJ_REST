# Generated by Django 3.1.3 on 2020-11-23 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('Stdid', models.IntegerField(primary_key=True, serialize=False)),
                ('Stdname', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'studenttable',
            },
        ),
    ]
