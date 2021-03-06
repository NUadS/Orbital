# Generated by Django 3.0.1 on 2020-05-25 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200523_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='dob',
            field=models.DateField(help_text='dd-mm-yyyy', verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='matriculationNumber',
            field=models.CharField(help_text='AXXXXXXXB', max_length=10, verbose_name='Matric Number'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='portfolio_site',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(upload_to='profile_pics'),
        ),
    ]
