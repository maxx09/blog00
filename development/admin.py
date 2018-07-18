from django.contrib import admin
from .models import Article, Comment, HashTag, Category

@admin.register(Article, HashTag, Category)
class ArticleAdmin(admin.ModelAdmin):

    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ['username', 'article', 'created_at', 'is_public']

class HashTag(admin.ModelAdmin):

    pass

class CategoryAdmin(admin.ModelAdmin):

    pass
