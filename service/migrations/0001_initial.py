# Generated by Django 4.0.4 on 2022-04-27 20:07

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advantage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('icon', models.ImageField(upload_to='advantages/', verbose_name='Icon')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Advantage',
                'verbose_name_plural': 'Advantages',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question', models.CharField(max_length=200, verbose_name='Question')),
                ('answer', ckeditor.fields.RichTextField(verbose_name='Answer')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Packet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Description')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('price_per', models.CharField(max_length=200, verbose_name='Price per')),
            ],
            options={
                'verbose_name': 'Packet',
                'verbose_name_plural': 'Packets',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('url', models.URLField(verbose_name='URL')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='projects/', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Specialist',
                'verbose_name_plural': 'Specialists',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('short_description', models.TextField(null=True)),
                ('full_description', ckeditor.fields.RichTextField(null=True)),
                ('icon', models.ImageField(null=True, upload_to='')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('advantages', models.ManyToManyField(related_name='services_advantages', to='service.advantage')),
                ('categories', models.ManyToManyField(related_name='services_categories', to='service.category')),
                ('packets', models.ManyToManyField(related_name='services_packets', to='service.packet')),
                ('projects', models.ManyToManyField(related_name='services_projects', to='service.project')),
                ('specialists', models.ManyToManyField(related_name='services_specialists', to='service.specialist')),
            ],
            options={
                'verbose_name': 'service',
                'verbose_name_plural': 'services',
                'ordering': ('title',),
            },
        ),
    ]
