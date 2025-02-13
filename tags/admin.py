from django.contrib import admin
from .models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'post_count')
    search_fields = ('name',)

    def post_count(self, obj):
        return obj.posts.count()
    post_count.short_description = 'Number of Posts'