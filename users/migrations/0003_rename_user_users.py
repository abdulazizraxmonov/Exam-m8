# Generated by Django 5.0.4 on 2024-05-05 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
    ]