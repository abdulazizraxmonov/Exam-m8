from rest_framework.response import Response
from rest_framework import viewsets, permissions, status
from .models import Papers_Category, Papers, PapersDetail, Reviews, Article, Keywords
from .serializers import PapersCategorySerializer, PapersSerializer, PapersDetailSerializer, ReviewsSerializer, ArticleSerializer, KeywordsSerializer
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import PapersFilter
import uuid
from django.db.models import F
from datetime import datetime, timedelta, timezone
from django.utils import timezone as django_timezone
from rest_framework.filters import SearchFilter, OrderingFilter


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.added_by == request.user


class PapersCategoryViewSet(viewsets.ModelViewSet):
    queryset = Papers_Category.objects.all()
    serializer_class = PapersCategorySerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['lang'] = self.request.GET.get('lang', 'uz')
        return context

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)


def generate_user_id():
    return str(uuid.uuid4())

class PapersViewSet(viewsets.ModelViewSet):
    queryset = Papers.objects.all()
    serializer_class = PapersSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = PapersFilter
    search_fields = ['title_uz', 'author', 'keywords__name', 'papersdetail__description_uz']
    ordering_fields = ['count']  

    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.query_params.get('ordering', None)
        if ordering == 'count':
            queryset = queryset.annotate(views_count=F('count')).order_by('-count')
        return queryset

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['lang'] = self.request.GET.get('lang', 'uz')
        return context

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        user_id = request.COOKIES.get('user_id')

        if not user_id:
            user_id = generate_user_id()
            response = Response('New user', status=status.HTTP_201_CREATED)
            response.set_cookie('user_id', user_id)
        else:
            response = Response('The user already exists', status=status.HTTP_200_OK)

        last_view_time_str = request.session.get('last_view_time')
        current_time = django_timezone.now()

        if last_view_time_str:
            last_view_time = datetime.strptime(last_view_time_str, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
        else:
            last_view_time = None

        if last_view_time is None or current_time - last_view_time > timedelta(seconds=10):
            queryset.update(count=F('count') + 1)
            request.session['last_view_time'] = current_time.strftime("%Y-%m-%d %H:%M:%S")

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return response

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)


class PapersDetailViewSet(viewsets.ModelViewSet):
    queryset = PapersDetail.objects.all()
    serializer_class = PapersDetailSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['lang'] = self.request.GET.get('lang', 'uz')
        return context

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['lang'] = self.request.GET.get('lang', 'uz')
        return context

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['lang'] = self.request.GET.get('lang', 'uz')
        return context

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)


class KeywordsViewSet(viewsets.ModelViewSet):
    queryset = Keywords.objects.all()
    serializer_class = KeywordsSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['lang'] = self.request.GET.get('lang', 'uz')
        return context

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)
