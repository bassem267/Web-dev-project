# Generated by Django 4.0.4 on 2022-05-23 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_course_alter_student_options_student_dateofbirth_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='dateOfBirth',
        ),
    ]