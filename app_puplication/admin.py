from django.contrib import admin
from .models import Publication, Tag, PublicationDetail

admin.site.register(Publication)
admin.site.register(Tag)
admin.site.register(PublicationDetail)
