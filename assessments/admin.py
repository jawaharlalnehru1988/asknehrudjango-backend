from django.contrib import admin
from .models import Topic, Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_filter = ['topic']
    search_fields = ['text']

admin.site.register(Topic)
admin.site.register(Choice)
