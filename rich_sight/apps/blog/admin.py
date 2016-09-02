from django.contrib import admin

from . import models


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'created', 'updated', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('updated', 'created', 'active')
    search_fields = ('name', 'email', 'body')

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment, CommentAdmin)


