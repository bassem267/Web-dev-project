# Generated by Django 4.0.4 on 2022-05-19 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='ID',
            new_name='courseID',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='department',
            new_name='studentDepartment',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='ID',
            new_name='studentID',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='studentName',
        ),
    ]
