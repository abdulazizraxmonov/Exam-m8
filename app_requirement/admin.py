from django.contrib import admin
from .models import Requirement, Part
from ckeditor.widgets import CKEditorWidget
from django import forms

class RequirementAdminForm(forms.ModelForm):
    text_uz = forms.CharField(widget=CKEditorWidget())
    text_ru = forms.CharField(widget=CKEditorWidget())
    text_en = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Requirement
        fields = '__all__'

class RequirementAdmin(admin.ModelAdmin):
    form = RequirementAdminForm

admin.site.register(Requirement, RequirementAdmin)
admin.site.register(Part)
