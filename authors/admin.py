from django.contrib import admin
from django.utils.html import format_html
from .models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'bod', 'display_image')
    search_fields = ('full_name', 'email')
    list_filter = ('bod',)
    fieldsets = (
        (None, {
            'fields': ('full_name', 'email', 'bod')
        }),
        ('Additional Info', {
            'fields': ('description', 'image'),
            'classes': ('collapse',)
        }),
    )

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "No Image"
    display_image.short_description = 'Profile Picture'