# Generated by Django 3.0.2 on 2020-01-28 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0002_auto_20200128_0605'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
