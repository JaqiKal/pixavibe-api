from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('owner', 'reason', 'created_at')


admin.site.register(Contact)
