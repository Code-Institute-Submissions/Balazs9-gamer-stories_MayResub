# Generated by Django 3.2 on 2022-05-18 20:33

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0002_commentstorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poststorie',
            name='posted_image',
            field=cloudinary.models.CloudinaryField(default='placeh', max_length=255, verbose_name='image'),
        ),
    ]