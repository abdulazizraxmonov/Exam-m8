from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PublicationViewSet, TagViewSet, PublicationDetailViewSet

router = DefaultRouter()
router.register(r'publications', PublicationViewSet)
router.register(r'tags', TagViewSet)
router.register(r'publicationdetails', PublicationDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
