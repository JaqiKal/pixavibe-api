from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin view for Category.
    """
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)
    list_per_page = (30)
