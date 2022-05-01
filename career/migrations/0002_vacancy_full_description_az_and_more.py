# Generated by Django 4.0.4 on 2022-05-01 19:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='full_description_az',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Full Description'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='full_description_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Full Description'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='full_description_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Full Description'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='short_description_az',
            field=models.TextField(null=True, verbose_name='Short Description'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='short_description_en',
            field=models.TextField(null=True, verbose_name='Short Description'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='short_description_ru',
            field=models.TextField(null=True, verbose_name='Short Description'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='title_az',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
    ]
