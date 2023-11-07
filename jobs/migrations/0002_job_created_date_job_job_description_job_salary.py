# Generated by Django 4.2.7 on 2023-11-04 11:43

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='job_description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
    ]