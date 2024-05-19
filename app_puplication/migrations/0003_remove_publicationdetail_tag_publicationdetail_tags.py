# Generated by Django 5.0.6 on 2024-05-18 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_puplication', '0002_publicationdetail_user_tag_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicationdetail',
            name='tag',
        ),
        migrations.AddField(
            model_name='publicationdetail',
            name='tags',
            field=models.ManyToManyField(related_name='details', to='app_puplication.tag'),
        ),
    ]
