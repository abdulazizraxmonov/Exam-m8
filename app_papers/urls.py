from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PapersCategoryViewSet, PapersViewSet, PapersDetailViewSet, ReviewsViewSet, ArticleViewSet, KeywordsViewSet

# Создаем экземпляр маршрутизатора
router = DefaultRouter()

# Регистрируем представления в маршрутизаторе
router.register(r'papers-categories', PapersCategoryViewSet)
router.register(r'papers', PapersViewSet)
router.register(r'papers-detail', PapersDetailViewSet)
router.register(r'reviews', ReviewsViewSet)
router.register(r'article', ArticleViewSet)
router.register(r'keywords', KeywordsViewSet)

urlpatterns = [
    # Добавляем маршруты из маршрутизатора в urlpatterns
    path('', include(router.urls)),
]
