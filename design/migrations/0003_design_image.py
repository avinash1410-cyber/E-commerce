# Generated by Django 4.0 on 2022-07-05 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0002_rename_user_design_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='design',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]