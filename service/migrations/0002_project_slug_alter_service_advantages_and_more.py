# Generated by Django 4.0.4 on 2022-04-27 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default='', max_length=200, unique=True, verbose_name='Slug'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='advantages',
            field=models.ManyToManyField(blank=True, related_name='services_advantages', to='service.advantage'),
        ),
        migrations.AlterField(
            model_name='service',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='services_categories', to='service.category'),
        ),
        migrations.AlterField(
            model_name='service',
            name='packets',
            field=models.ManyToManyField(blank=True, related_name='services_packets', to='service.packet'),
        ),
        migrations.AlterField(
            model_name='service',
            name='projects',
            field=models.ManyToManyField(blank=True, related_name='services_projects', to='service.project'),
        ),
        migrations.AlterField(
            model_name='service',
            name='specialists',
            field=models.ManyToManyField(blank=True, related_name='services_specialists', to='service.specialist'),
        ),
    ]
