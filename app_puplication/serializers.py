from rest_framework import serializers
from .models import Publication, Tag, PublicationDetail

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name_uz', 'name_ru', 'name_en']

class PublicationDetailSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = PublicationDetail
        fields = ['id', 'description_uz', 'description_ru', 'description_en', 'tags', 'publication_text', 'publication_file']


class PublicationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    tags = TagSerializer(many=True) 
    details = PublicationDetailSerializer(many=True) 

    class Meta:
        model = Publication
        fields = ['id', 'user', 'publication_photo', 'description_uz', 'description_ru', 'description_en', 'tags', 'details']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        details_data = validated_data.pop('details')
        publication = Publication.objects.create(**validated_data)

        for tag_data in tags_data:
            Tag.objects.create(publication=publication, **tag_data)

        for detail_data in details_data:
            PublicationDetail.objects.create(publication=publication, **detail_data)

        return publication
