# Generated by Django 4.0.4 on 2022-04-29 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_aboutusteam_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutusteam',
            name='is_active',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is active'),
        ),
    ]