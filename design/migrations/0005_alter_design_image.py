# Generated by Django 4.0.1 on 2022-07-27 10:23

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0004_alter_design_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
