# Generated by Django 4.2.7 on 2023-11-09 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscribe',
            old_name='firstname',
            new_name='first_name',
        ),
    ]
