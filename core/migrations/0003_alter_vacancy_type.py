# Generated by Django 4.0.4 on 2022-04-27 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_vacancy_applicant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='type',
            field=models.IntegerField(choices=[('full_time', 'Full time'), ('part_time', 'Part time'), ('internship', 'Internship')], verbose_name='Type'),
        ),
    ]
