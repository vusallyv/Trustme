# Generated by Django 4.0.4 on 2022-05-01 19:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_alter_applicant_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='full_description_az',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='full_description_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='full_description_ru',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='short_description_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='short_description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='short_description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='title_az',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='title_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='serviceadvantage',
            name='description_az',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='serviceadvantage',
            name='description_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='serviceadvantage',
            name='description_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='serviceadvantage',
            name='title_az',
            field=models.CharField(max_length=200, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='serviceadvantage',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='serviceadvantage',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='servicecategory',
            name='answer_az',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Answer'),
        ),
        migrations.AddField(
            model_name='servicecategory',
            name='answer_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Answer'),
        ),
        migrations.AddField(
            model_name='servicecategory',
            name='answer_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Answer'),
        ),
        migrations.AddField(
            model_name='servicecategory',
            name='question_az',
            field=models.CharField(max_length=200, null=True, verbose_name='Question'),
        ),
        migrations.AddField(
            model_name='servicecategory',
            name='question_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Question'),
        ),
        migrations.AddField(
            model_name='servicecategory',
            name='question_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Question'),
        ),
        migrations.AddField(
            model_name='servicepacket',
            name='description_az',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='servicepacket',
            name='description_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='servicepacket',
            name='description_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='servicepacket',
            name='price_per_az',
            field=models.CharField(max_length=200, null=True, verbose_name='Price per'),
        ),
        migrations.AddField(
            model_name='servicepacket',
            name='price_per_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Price per'),
        ),
        migrations.AddField(
            model_name='servicepacket',
            name='price_per_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Price per'),
        ),
        migrations.AddField(
            model_name='servicepacket',
            name='title_az',
            field=models.CharField(max_length=200, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='servicepacket',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='servicepacket',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='servicespecialist',
            name='description_az',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='servicespecialist',
            name='description_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='servicespecialist',
            name='description_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='servicespecialist',
            name='name_az',
            field=models.CharField(max_length=200, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='servicespecialist',
            name='name_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='servicespecialist',
            name='name_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Name'),
        ),
    ]
