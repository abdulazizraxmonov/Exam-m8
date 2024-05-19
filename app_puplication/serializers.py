from rest_framework import serializers
from .models import Publication, Tag, PublicationDetail

class TagSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = ['id', 'name']

    def get_name(self, obj):
        lang = self.context.get('lang', 'uz')
        if lang == 'ru':
            return obj.name_ru
        elif lang == 'en':
            return obj.name_en
        return obj.name_uz

class PublicationDetailSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    tags = TagSerializer(many=True)

    class Meta:
        model = PublicationDetail
        fields = ['id', 'description', 'tags', 'publication_text', 'publication_file']

    def get_description(self, obj):
        lang = self.context.get('lang', 'uz')
        if lang == 'ru':
            return obj.description_ru
        elif lang == 'en':
            return obj.description_en
        return obj.description_uz

class PublicationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    description = serializers.SerializerMethodField()
    tags = TagSerializer(many=True) 
    details = PublicationDetailSerializer(many=True) 

    class Meta:
        model = Publication
        fields = ['id', 'user', 'publication_photo', 'description', 'tags', 'details']

    def get_description(self, obj):
        lang = self.context.get('lang', 'uz')
        if lang == 'ru':
            return obj.description_ru
        elif lang == 'en':
            return obj.description_en
        return obj.description_uz

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        details_data = validated_data.pop('details')
        publication = Publication.objects.create(**validated_data)

        for tag_data in tags_data:
            Tag.objects.create(publication=publication, **tag_data)

        for detail_data in details_data:
            PublicationDetail.objects.create(publication=publication, **detail_data)

        return publication
