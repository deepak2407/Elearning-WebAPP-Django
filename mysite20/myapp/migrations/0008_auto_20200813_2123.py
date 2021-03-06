# Generated by Django 3.0.7 on 2020-08-14 01:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_course_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='img',
            field=models.ImageField(default='myapp/static/myapp/noimg.png', upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(100)]),
        ),
    ]
