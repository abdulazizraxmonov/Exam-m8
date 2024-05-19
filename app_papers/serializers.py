from rest_framework import serializers
from .models import Papers, Papers_Category, PapersDetail, Reviews, Article, Keywords

class PapersCategorySerializer(serializers.ModelSerializer):
    subject_name = serializers.SerializerMethodField()

    class Meta:
        model = Papers_Category
        fields = ['id', 'subject_name']

    def get_subject_name(self, obj):
        lang = self.context.get('lang', 'uz')
        if lang == 'ru':
            return obj.subject_name_ru
        elif lang == 'en':
            return obj.subject_name_en
        return obj.subject_name_uz


class PapersDetailSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = PapersDetail
        fields = ['id', 'description', 'category', 'date', 'author', 'pdffile']

    def get_description(self, obj):
        lang = self.context.get('lang', 'uz')
        if lang == 'ru':
            return obj.description_ru
        elif lang == 'en':
            return obj.description_en
        return obj.description_uz


class ReviewsSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()

    class Meta:
        model = Reviews
        fields = ['id', 'user_name', 'content', 'article']

    def get_content(self, obj):
        lang = self.context.get('lang', 'uz')
        if lang == 'ru':
            return obj.content_ru
        elif lang == 'en':
            return obj.content_en
        return obj.content_uz


class ArticleSerializer(serializers.ModelSerializer):
    article_text = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id', 'article_text', 'papers_detail']

    def get_article_text(self, obj):
        lang = self.context.get('lang', 'uz')
        if lang == 'ru':
            return obj.article_text_ru
        elif lang == 'en':
            return obj.article_text_en
        return obj.article_text_uz


class KeywordsSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Keywords
        fields = ['id', 'name']

    def get_name(self, obj):
        lang = self.context.get('lang', 'uz')
        if lang == 'ru':
            return obj.name_ru
        elif lang == 'en':
            return obj.name_en
        return obj.name_uz


class PapersSerializer(serializers.ModelSerializer):
    category = PapersCategorySerializer()
    papersdetail_set = PapersDetailSerializer(many=True, read_only=True)
    article_set = ArticleSerializer(many=True, read_only=True)
    keywords_set = KeywordsSerializer(many=True, read_only=True)

    class Meta:
        model = Papers
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        lang = kwargs.pop('lang', None)
        super().__init__(*args, **kwargs)
        self.lang = lang

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if self.lang:
            data['category'] = PapersCategorySerializer(instance.category, context={'lang': self.lang}).data
            data['papersdetail_set'] = PapersDetailSerializer(instance.papersdetail_set.all(), many=True, context={'lang': self.lang}).data
            data['article_set'] = ArticleSerializer(instance.article_set.all(), many=True, context={'lang': self.lang}).data
            data['keywords_set'] = KeywordsSerializer(instance.keywords_set.all(), many=True, context={'lang': self.lang}).data
            if 'reviews_set' in data:
                data['reviews_set'] = sorted(data['reviews_set'], key=lambda x: x['user_name'])
        return data
