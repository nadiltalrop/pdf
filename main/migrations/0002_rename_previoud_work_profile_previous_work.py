# Generated by Django 4.2.5 on 2023-09-08 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='previoud_work',
            new_name='previous_work',
        ),
    ]