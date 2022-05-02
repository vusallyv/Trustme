# Generated by Django 3.2.13 on 2022-05-01 14:04

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('type', models.CharField(choices=[('Full time', 'Full time'), ('Part time', 'Part time'), ('Internship', 'Internship')], default='full_time', max_length=255, verbose_name='Type')),
                ('short_description', models.TextField(verbose_name='Short Description')),
                ('full_description', ckeditor.fields.RichTextField(verbose_name='Full Description')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Vacancy',
                'verbose_name_plural': 'Vacancies',
                'db_table': 'vacancy',
            },
        ),
    ]