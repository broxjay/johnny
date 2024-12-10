from django.contrib import admin
from .models import Blog


class Blogadmin(admin.ModelAdmin):
    list_display = ['id', "title", "image", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["title", "content"]

admin.site.register(Blog, Blogadmin)
