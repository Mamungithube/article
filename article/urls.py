from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MultimediaExampleViewSet, 
    NewsArticleViewSet, 
    MediaAssetViewSet,
    SidebarSectionViewSet
)

# Using DefaultRouter for automatic URL routing for ViewSets
router = DefaultRouter()

# Endpoint for top multimedia buttons (Text, Image, Audio, etc.)
router.register(r'multimedia-examples', MultimediaExampleViewSet, basename='multimedia-example')

# Endpoint for the main News Articles and Sidebar Content
router.register(r'articles', NewsArticleViewSet, basename='article')

# Endpoint for uploading and managing Media Assets
router.register(r'media-assets', MediaAssetViewSet, basename='media-asset')

router.register(r'sidebar-sections', SidebarSectionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]