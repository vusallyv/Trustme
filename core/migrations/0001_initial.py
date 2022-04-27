# Generated by Django 4.0.4 on 2022-04-27 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=255, verbose_name='Full name')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('company_name', models.CharField(max_length=255, verbose_name='Company name')),
                ('phone_prefix', models.IntegerField(choices=[('+994', '+994'), ('+7', '+7'), ('+1', '+1')], default='+994', verbose_name='Phone prefix')),
                ('phone', models.CharField(max_length=30, verbose_name='Phone')),
                ('message', models.TextField(verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
                'db_table': 'contact',
            },
        ),
    ]
