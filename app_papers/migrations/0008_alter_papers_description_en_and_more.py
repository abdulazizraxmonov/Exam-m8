# Generated by Django 5.0.6 on 2024-05-19 00:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_papers', '0007_alter_keywords_papers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='papers',
            name='description_en',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='papers',
            name='description_ru',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='papers',
            name='description_uz',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
