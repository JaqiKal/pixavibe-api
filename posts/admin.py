from django.contrib import admin
from .models import Post
from tags.models import Tag

# Customize the Post admin to manage the Many-to-Many relationship with tags
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title', 'content')
    filter_horizontal = ('tags',)  # widget for managing Many-to-Many relationships

admin.site.register(Post)
