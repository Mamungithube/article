import mimetypes
from rest_framework import serializers
from .models import MultimediaExample, NewsArticle, SidebarSection, MediaAsset

class MediaAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaAsset
        fields = '__all__'

    def validate(self, data):
        file = data.get('file')
        file_type = data.get('file_type')

        # Logic 1: Disallow file upload for text/youtube types
        if file and file_type in ['text', 'youtube']:
            raise serializers.ValidationError({"file_type": f"Files cannot be uploaded for '{file_type}' type."})

        # Logic 2: Mime-type validation for physical files
        if file:
            mime_type, _ = mimetypes.guess_type(file.name)
            if not mime_type:
                raise serializers.ValidationError({"file": "Invalid file format."})

            type_mapping = {
                'image': 'image/',
                'video': 'video/',
                'audio': 'audio/'
            }

            expected_prefix = type_mapping.get(file_type)
            if expected_prefix and not mime_type.startswith(expected_prefix):
                raise serializers.ValidationError({"file_type": f"File content does not match type '{file_type}'."})

        return data

class MultimediaExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultimediaExample
        fields = '__all__'

class SidebarSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SidebarSection
        fields = '__all__'

class NewsArticleSerializer(serializers.ModelSerializer):
    sidebar_sections = SidebarSectionSerializer(many=True, read_only=True)

    class Meta:
        model = NewsArticle
        fields = '__all__'