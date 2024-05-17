from rest_framework import serializers
from .models import FAQ, Answer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    
    class Meta:
        model = FAQ
        fields = '__all__'
