# Generated by Django 3.2 on 2022-01-24 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20220120_1602'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='textbox',
            new_name='your_comment',
        ),
    ]