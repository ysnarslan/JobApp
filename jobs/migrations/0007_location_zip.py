# Generated by Django 4.2.7 on 2023-11-07 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_location_job_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='zip',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
