from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AudioViewSet

router = DefaultRouter()
router.register(r'audios', AudioViewSet, basename='audio')

urlpatterns = [
    path('', include(router.urls)),
]
