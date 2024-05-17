from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FAQViewSet, AnswerViewSet

router = DefaultRouter()
router.register(r'faq', FAQViewSet)
router.register(r'answer', AnswerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
