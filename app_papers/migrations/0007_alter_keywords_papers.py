# Generated by Django 5.0.6 on 2024-05-19 00:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_papers', '0006_papers_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keywords',
            name='papers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keywords', to='app_papers.papers'),
        ),
    ]
