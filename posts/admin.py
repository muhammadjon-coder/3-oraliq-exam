from django.contrib import admin
from .models import Post, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'catalog', 'created_at', 'updated_at', 'comment_count')
    list_filter = ('catalog', 'author', 'tag', 'created_at')
    search_fields = ('name', 'description', 'author__full_name')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [CommentInline]
    filter_horizontal = ('tag',)

    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'author', 'catalog')
        }),
        ('Content', {
            'fields': ('description', 'image')
        }),
        ('Tags', {
            'fields': ('tag',)
        }),
    )

    def comment_count(self, obj):
        return obj.comments.count()
    comment_count.short_description = 'Comments'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'comment', 'post__name')