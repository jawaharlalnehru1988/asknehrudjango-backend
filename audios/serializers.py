from rest_framework import serializers
from .models import Audio

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ['id', 'audioTitle', 'description', 'language', 'filePath', 'audioImage', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
