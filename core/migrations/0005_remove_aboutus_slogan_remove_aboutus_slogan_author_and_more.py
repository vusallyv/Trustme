# Generated by Django 4.0.4 on 2022-05-10 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_testimonial_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='slogan',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='slogan_author',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='slogan_author_az',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='slogan_author_en',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='slogan_author_ru',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='slogan_az',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='slogan_en',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='slogan_ru',
        ),
        migrations.CreateModel(
            name='AboutUsSlogan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slogan', models.TextField(verbose_name='Slogan')),
                ('slogan_en', models.TextField(null=True, verbose_name='Slogan')),
                ('slogan_az', models.TextField(null=True, verbose_name='Slogan')),
                ('slogan_ru', models.TextField(null=True, verbose_name='Slogan')),
                ('slogan_author', models.CharField(max_length=255, verbose_name='Slogan author')),
                ('slogan_author_en', models.CharField(max_length=255, null=True, verbose_name='Slogan author')),
                ('slogan_author_az', models.CharField(max_length=255, null=True, verbose_name='Slogan author')),
                ('slogan_author_ru', models.CharField(max_length=255, null=True, verbose_name='Slogan author')),
                ('about_us', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='about_us_slogan', to='core.aboutus', verbose_name='About us')),
            ],
            options={
                'verbose_name': 'About Us Slogan',
                'verbose_name_plural': 'About Us Slogan',
                'db_table': 'about_us_slogan',
            },
        ),
    ]
