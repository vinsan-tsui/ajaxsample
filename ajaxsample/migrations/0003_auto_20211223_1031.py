# Generated by Django 3.1.5 on 2021-12-23 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajaxsample', '0002_auto_20211223_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='dob',
            field=models.DateField(),
        ),
    ]