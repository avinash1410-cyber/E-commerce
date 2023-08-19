# Generated by Django 4.2.4 on 2023-08-19 04:32

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0005_alter_design_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
