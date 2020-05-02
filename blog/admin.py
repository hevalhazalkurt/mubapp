from django.contrib import admin
from .models import Post, PostCategory


admin.site.register(Post)
admin.site.register(PostCategory)
