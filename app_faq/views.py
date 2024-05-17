from .models import FAQ, Answer
from .serializers import FAQSerializer, AnswerSerializer
from rest_framework import viewsets

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer