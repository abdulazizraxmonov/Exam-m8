from django.db import models

class FAQ(models.Model):
    question_uz = models.CharField(max_length=255, verbose_name='Savol (Uzbek)')
    question_ru = models.CharField(max_length=255, verbose_name='Вопрос (Russian)')
    question_en = models.CharField(max_length=255, verbose_name='Question (English)')

    def __str__(self):
        return self.question_uz


class Answer(models.Model):
    faq = models.ForeignKey(FAQ, on_delete=models.CASCADE, related_name='answers')
    answer_uz = models.TextField(verbose_name='Javob (Uzbek)')
    answer_ru = models.TextField(verbose_name='Ответ (Russian)')
    answer_en = models.TextField(verbose_name='Answer (English)')
    
    def __str__(self):
        return self.answer_uz
