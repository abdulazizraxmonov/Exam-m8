from django.db import models

class Contact(models.Model):
    firstname = models.CharField(max_length=100)
    email = models.EmailField(verbose_name='E-mail')
    message = models.TextField()

    def __str__(self):
        return self.firstname
    
