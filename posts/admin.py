from django.contrib import admin
from .models import Post
from hashtags.models import Hashtag


# Customize the Post admin to manage the Many-to-Many relationship with tags
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title', 'content')
    filter_horizontal = ('hashtags',)  # widget managing Many-to-Many rel-ships


admin.site.register(Post)
