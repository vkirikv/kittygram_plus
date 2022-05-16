# kittygram_plus/urls.py
from django.urls import include, path
# from rest_framework.authtoken import views - Для обычного токена
from rest_framework.routers import DefaultRouter

from cats.views import CatViewSet, OwnerViewSet


router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # path('api-token-auth/', views.obtain_auth_token), - Для обычного токена
]
