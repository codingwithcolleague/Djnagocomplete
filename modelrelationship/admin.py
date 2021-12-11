from django.contrib import admin
from django.db import models

# Register your models here.
from .models import Page,Like,Post,Song

@admin.register(Page)
class PageModel(admin.ModelAdmin):
    list_display = ['user','page_name','page_cat','page_publish']

@admin.register(Like)
class PageModel(admin.ModelAdmin):
    list_display = ['user','page_name','page_cat','page_publish','likes']

@admin.register(Post)
class PostModel(admin.ModelAdmin):
    list_display = ['user','post_title','post_cat','post_publish_date']


@admin.register(Song)
class SongModel(admin.ModelAdmin):
    list_display = ['song_name','song_duration','written_by']