# Generated by Django 5.0.6 on 2024-05-17 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_faq', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='question_en',
            field=models.CharField(max_length=255, verbose_name='Question (English)'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_ru',
            field=models.CharField(max_length=255, verbose_name='Вопрос (Russian)'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_uz',
            field=models.CharField(max_length=255, verbose_name='Savol (Uzbek)'),
        ),
    ]
