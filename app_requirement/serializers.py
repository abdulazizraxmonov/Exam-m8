from rest_framework import serializers
from .models import Requirement, Part

class PartSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = Part
        fields = ['id', 'requirement', 'partnumber', 'description']

    def get_description(self, obj):
        lang = self.context.get('lang', 'uz')
        if lang == 'ru':
            return obj.description_ru
        elif lang == 'en':
            return obj.description_en
        return obj.description_uz

class RequirementSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    text = serializers.SerializerMethodField()
    parts = PartSerializer(many=True, read_only=True)

    class Meta:
        model = Requirement
        fields = ['id', 'title', 'text', 'parts']

    def get_title(self, obj):
        lang = self.context.get('lang', 'uz')
        if lang == 'ru':
            return obj.title_ru
        elif lang == 'en':
            return obj.title_en
        return obj.title_uz

    def get_text(self, obj):
        lang = self.context.get('lang', 'uz')
        if lang == 'ru':
            return obj.text_ru
        elif lang == 'en':
            return obj.text_en
        return obj.text_uz
