import os
import uuid
from django.db import models

def get_file_path(instance, filename):
    """Generates a unique path for uploaded files using UUID to avoid long filename errors."""
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('media_assets/', filename)

class MultimediaExample(models.Model):
    TYPE_CHOICES = (
        ('text', 'Text'),
        ('image', 'Image'),
        ('audio', 'Audio'),
        ('video', 'Video'),
        ('youtube', 'YouTube'),
    )
    title = models.CharField(max_length=50)
    media_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    icon_type = models.CharField(max_length=50, default="search")
    
    def __str__(self):
        return self.title

class NewsArticle(models.Model):
    title = models.CharField(max_length=255, default="News Article with Interactive Elements")
    content_data = models.JSONField(help_text="Stores structured text and interactive element markers")
    youtube_embedded_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class SidebarSection(models.Model):
    article = models.ForeignKey(NewsArticle, related_name='sidebar_sections', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_expanded = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

class MediaAsset(models.Model):
    MEDIA_TYPES = (
        ('image', 'Image'),
        ('audio', 'Audio'),
        ('video', 'Video'),
        ('text', 'Text'),
        ('youtube', 'YouTube'),
    )
    file = models.FileField(upload_to=get_file_path, max_length=500, null=True, blank=True)
    file_type = models.CharField(max_length=20, choices=MEDIA_TYPES)
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.file_type} - {self.caption}"