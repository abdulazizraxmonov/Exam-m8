from django.db import models
from ckeditor.fields import RichTextField

class Requirement(models.Model):
    title_uz = models.CharField(max_length=200)
    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    text_uz = RichTextField()
    text_ru = RichTextField()
    text_en = RichTextField()

    def __str__(self):
        return self.title_uz
    

class Part(models.Model):
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE, related_name='parts')
    partnumber = models.CharField(max_length=50)
    description_uz = models.TextField()
    description_ru = models.TextField()
    description_en = models.TextField()

    def __str__(self):
        return self.partnumber
