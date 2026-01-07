from django.contrib import admin
from .models import Audio

@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ['id', 'audioTitle', 'language', 'created_at']
    list_filter = ['language', 'created_at']
    search_fields = ['audioTitle', 'description']

