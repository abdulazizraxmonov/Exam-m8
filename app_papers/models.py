from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField

class Papers_Category(models.Model):
    subject_name_uz = models.CharField(max_length=255)
    subject_name_ru = models.CharField(max_length=255)
    subject_name_en = models.CharField(max_length=255)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.subject_name_uz


class Papers(models.Model):
    category = models.ForeignKey(Papers_Category, on_delete=models.CASCADE)
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    date = models.DateField()
    author = models.CharField(max_length=255)
    description_uz = RichTextField()
    description_ru = RichTextField()
    description_en = RichTextField()
    count = models.PositiveIntegerField(default=0)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title_uz
    
class PapersDetail(models.Model):
    papers = models.ForeignKey(Papers, on_delete=models.CASCADE)
    category = models.ForeignKey(Papers_Category, on_delete=models.CASCADE)
    date = models.DateField()
    author = models.CharField(max_length=255)
    description_uz = RichTextField()
    description_ru = RichTextField()
    description_en = RichTextField()
    pdffile = models.FileField(upload_to='papers/')
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.description_uz
    
class Reviews(models.Model):
    user_name = models.CharField(max_length=255)
    content_uz = RichTextField()
    content_ru = RichTextField()
    content_en = RichTextField()
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.content_uz

class Article(models.Model):
    article_text_uz = RichTextField()
    article_text_ru = RichTextField()
    article_text_en = RichTextField()
    papers_detail = models.ForeignKey(PapersDetail, on_delete=models.CASCADE)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.article_text_uz

class Keywords(models.Model):
    papers = models.ForeignKey(Papers, related_name='keywords', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    

class UserPaperView(models.Model):
    user_id = models.CharField(max_length=255)
    paper_id = models.IntegerField()
    last_viewed = models.DateTimeField()