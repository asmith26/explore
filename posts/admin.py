from django.contrib import admin
from .models import SubReddit, Post, Comment

admin.site.register(SubReddit)
admin.site.register(Post)
admin.site.register(Comment)
