import django_filters
from .models import Papers, Keywords, PapersDetail

class PapersFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title_uz', lookup_expr='icontains')
    author = django_filters.CharFilter(field_name='author', lookup_expr='icontains')
    keyword = django_filters.CharFilter(field_name='keywords__name', lookup_expr='icontains')

    class Meta:
        model = Papers
        fields = ['title', 'author', 'keyword']
