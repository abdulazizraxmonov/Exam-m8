# Generated by Django 5.0.6 on 2024-05-17 02:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_faq', '0002_alter_faq_question_en_alter_faq_question_ru_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='faq',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='app_faq.faq'),
        ),
    ]
