# Generated by Django 4.0.4 on 2022-04-28 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicepacket',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Is main'),
        ),
    ]
