from django.contrib import admin
from .models import MultimediaExample, NewsArticle, SidebarSection, MediaAsset

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

admin.site.register(MultimediaExample)
admin.site.register(SidebarSection)
admin.site.register(MediaAsset)