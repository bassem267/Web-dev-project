# Generated by Django 4.0.4 on 2022-05-23 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_student_university'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseID', models.CharField(blank=True, max_length=15)),
                ('department', models.CharField(blank=True, max_length=250)),
                ('courseName', models.CharField(blank=True, max_length=150)),
                ('numberOfHours', models.IntegerField(blank=True)),
                ('lectureDay', models.CharField(blank=True, max_length=150)),
                ('hallNumber', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'ordering': ['courseName'],
            },
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['studentName']},
        ),
        migrations.AddField(
            model_name='student',
            name='dateOfBirth',
            field=models.DateField(default='2001-6-15'),
        ),
        migrations.AddField(
            model_name='student',
            name='gendar',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='studentDepartment',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentID',
            field=models.CharField(blank=True, max_length=150, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentName',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='student',
            name='university',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
