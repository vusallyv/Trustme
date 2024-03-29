# Generated by Django 4.0.4 on 2022-05-07 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0011_service_full_description_az_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='phone_prefix',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Phone prefix'),
        ),
    ]
