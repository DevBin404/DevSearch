# Generated by Django 3.2.16 on 2023-01-08 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20230107_1918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='short_info',
            new_name='short_intro',
        ),
    ]
