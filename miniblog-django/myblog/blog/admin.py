from django.contrib import admin
from .models import Post, Comments

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')

@admin.register(Comments)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'post')

# Register your models here.
