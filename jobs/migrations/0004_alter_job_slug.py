# Generated by Django 4.2.7 on 2023-11-06 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_job_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='slug',
            field=models.SlugField(max_length=40, null=True, unique=True),
        ),
    ]