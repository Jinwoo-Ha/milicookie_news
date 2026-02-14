from django.contrib import admin
from .models import Newsletter

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'sent_count')
    search_fields = ('title', 'content')
    list_filter = ('published_at',)
    readonly_fields = ('published_at', 'sent_count')

