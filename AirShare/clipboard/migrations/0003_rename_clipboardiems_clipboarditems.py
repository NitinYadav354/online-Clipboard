# Generated by Django 5.1.2 on 2024-10-11 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clipboard', '0002_alter_clipboardiems_uniquecode'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clipboardiems',
            new_name='ClipboardItems',
        ),
    ]
