from rest_framework import serializers
from .models import Papers, Papers_Category, PapersDetail, Reviews, Article, Keywords

class PapersCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Papers_Category
        fields = '__all__'

class PapersDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PapersDetail
        fields = '__all__'

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class KeywordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keywords
        fields = ['name']

class PapersSerializer(serializers.ModelSerializer):
    category = PapersCategorySerializer()
    papersdetail_set = PapersDetailSerializer(many=True, read_only=True)
    article_set = ArticleSerializer(many=True, read_only=True)
    keywords_set = KeywordsSerializer(many=True, read_only=True)

    class Meta:
        model = Papers
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if 'reviews_set' in data:
            data['reviews_set'] = sorted(data['reviews_set'], key=lambda x: x['user_name'])
        return data
