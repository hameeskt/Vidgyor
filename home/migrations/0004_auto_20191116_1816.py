# Generated by Django 2.2.7 on 2019-11-16 12:46

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20191114_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='uploaded_by',
            field=models.CharField(default=django.contrib.auth.models.User, max_length=30),
        ),
    ]