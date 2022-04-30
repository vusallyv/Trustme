# Generated by Django 4.0.4 on 2022-04-30 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_contact_phone_prefix_alter_vacancy_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutusinfo',
            name='icon',
            field=models.ImageField(upload_to='about_us_info/', verbose_name='Icon'),
        ),
        migrations.AlterField(
            model_name='aboutusinfo',
            name='mobile_icon',
            field=models.ImageField(upload_to='about_us_info/', verbose_name='Mobile icon'),
        ),
        migrations.AlterField(
            model_name='aboutusteam',
            name='image',
            field=models.ImageField(upload_to='about_us_team/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='cv',
            field=models.FileField(upload_to='cv/', verbose_name='CV'),
        ),
    ]