# Generated by Django 3.2.13 on 2022-05-01 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0001_initial'),
        ('service', '0004_auto_20220501_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.service', verbose_name='Service'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='vacancy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='career.vacancy', verbose_name='Vacancy'),
        ),
    ]
