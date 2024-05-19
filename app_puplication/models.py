from django.conf import settings
from django.db import models
from ckeditor.fields import RichTextField

class Publication(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    publication_photo = models.ImageField(upload_to='publications/')
    description_uz = RichTextField()
    description_ru = RichTextField()
    description_en = RichTextField()
    last_edit = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"Publication {self.id}"
    
class Tag(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    publications = models.ManyToManyField(Publication, related_name='tags')

    def __str__(self):
        return self.name_en

class PublicationDetail(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='details')
    description_uz = RichTextField()
    description_ru = RichTextField()
    description_en = RichTextField()
    tags = models.ManyToManyField(Tag, related_name='details')
    publication_text = RichTextField()
    publication_file = models.FileField(upload_to='publication_files/', blank=True, null=True)

    def __str__(self):
        return f"Detail for {self.publication.id}"
