from rest_framework import viewsets, filters
from django.core.exceptions import PermissionDenied
from .models import Publication, Tag, PublicationDetail
from .serializers import PublicationSerializer, TagSerializer, PublicationDetailSerializer
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['description_uz', 'description_ru', 'description_en']
    search_fields = ['description_uz', 'description_ru', 'description_en']
    ordering_fields = ['id', 'last_edit'] 

    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.query_params.get('ordering', None)
        if ordering == 'last_edit':
            queryset = queryset.order_by('-last_edit')
        return queryset

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['lang'] = self.request.GET.get('lang', 'uz')
        return context

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        if self.request.user == self.get_object().user:
            serializer.save()
        else:
            raise PermissionDenied("You can only edit your own publications.")

    def perform_destroy(self, instance):
        if self.request.user == instance.user:
            instance.delete()
        else:
            raise PermissionDenied("You can only delete your own publications.")


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name_uz', 'name_ru', 'name_en']
    search_fields = ['name_uz', 'name_ru', 'name_en']
    ordering_fields = ['name_uz', 'name_ru', 'name_en']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['lang'] = self.request.GET.get('lang', 'uz')
        return context

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        if self.request.user == self.get_object().user:
            serializer.save()
        else:
            raise PermissionDenied("You can only edit your own tags.")

    def perform_destroy(self, instance):
        if self.request.user == instance.user:
            instance.delete()
        else:
            raise PermissionDenied("You can only delete your own tags.")


class PublicationDetailViewSet(viewsets.ModelViewSet):
    queryset = PublicationDetail.objects.all()
    serializer_class = PublicationDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['publication', 'description_uz', 'description_ru', 'description_en', 'tags']
    search_fields = ['description_uz', 'description_ru', 'description_en', 'publication_text']
    ordering_fields = ['publication', 'description_uz', 'description_ru', 'description_en']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['lang'] = self.request.GET.get('lang', 'uz')
        return context

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        if self.request.user == self.get_object().user:
            serializer.save()
        else:
            raise PermissionDenied("You can only edit your own publication details.")

    def perform_destroy(self, instance):
        if self.request.user == instance.user:
            instance.delete()
        else:
            raise PermissionDenied("You can only delete your own publication details.")
