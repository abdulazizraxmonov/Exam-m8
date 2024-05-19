from django.contrib import admin
from .models import Papers_Category, Papers, PapersDetail, Reviews, Article, Keywords

admin.site.register(Papers_Category)
admin.site.register(Papers)
admin.site.register(PapersDetail)
admin.site.register(Reviews)
admin.site.register(Article)
admin.site.register(Keywords)

