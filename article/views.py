from rest_framework import viewsets
from .models import MultimediaExample, NewsArticle, MediaAsset, SidebarSection
from .serializers import (
    MultimediaExampleSerializer, 
    NewsArticleSerializer, 
    MediaAssetSerializer, 
    SidebarSectionSerializer
)

class MultimediaExampleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MultimediaExample.objects.all()
    serializer_class = MultimediaExampleSerializer

class NewsArticleViewSet(viewsets.ModelViewSet):
    queryset = NewsArticle.objects.all().prefetch_related('sidebar_sections')
    serializer_class = NewsArticleSerializer

class MediaAssetViewSet(viewsets.ModelViewSet):
    queryset = MediaAsset.objects.all()
    serializer_class = MediaAssetSerializer

class SidebarSectionViewSet(viewsets.ModelViewSet):
    queryset = SidebarSection.objects.all()
    serializer_class = SidebarSectionSerializer