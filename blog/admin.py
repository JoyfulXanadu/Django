from django.contrib import admin
from blog.models import Article

@admin.register(Article)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "slug", "created_at", "is_published", "views_count")
