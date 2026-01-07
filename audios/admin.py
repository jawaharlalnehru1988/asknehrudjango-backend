from django.contrib import admin
from django.utils.html import format_html
from .models import Audio

@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ['id', 'audioTitle', 'language', 'audio_image_preview', 'has_audio_file', 'created_at', 'updated_at']
    list_filter = ['language', 'created_at']
    search_fields = ['audioTitle', 'description', 'language']
    ordering = ['-created_at']
    readonly_fields = ['audio_image_preview', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Audio Information', {
            'fields': ('audioTitle', 'description', 'language')
        }),
        ('Media Files', {
            'fields': ('filePath', 'audioImage', 'audio_image_preview')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def audio_image_preview(self, obj):
        if obj.audioImage:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 150px;" />', obj.audioImage.url)
        return "No image"
    audio_image_preview.short_description = 'Image Preview'
    
    def has_audio_file(self, obj):
        if obj.filePath:
            return format_html('<span style="color: green;">✓ Yes</span>')
        return format_html('<span style="color: red;">✗ No</span>')
    has_audio_file.short_description = 'Audio File'
