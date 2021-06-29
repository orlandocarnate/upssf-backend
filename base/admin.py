from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

# class PostAdmin(SummernoteModelAdmin):
#     summernote_fields = ('body',)

# Register your models here.
# admin.site.register(Post, PostAdmin)
# admin.site.register(Post, PostAdmin)

# @admin.register(Article, ArticleAdmin)
class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
    list_display = ('title', 'slug', 'officer', 'publishDate', 'status')
    search_fields = ('title', 'body')
    prepopulated_fields = { 'slug': ('title',) }
    raw_id_fields = ('officer',)
    date_hierarchy = 'publishDate'
    ordering = ('status', 'publishDate')

class ScholarAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Scholar, ScholarAdmin)
admin.site.register(Officer)