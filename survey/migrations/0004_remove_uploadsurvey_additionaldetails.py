# Generated by Django 3.0.1 on 2020-06-07 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_uploadsurvey_additionaldetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadsurvey',
            name='additionaldetails',
        ),
    ]