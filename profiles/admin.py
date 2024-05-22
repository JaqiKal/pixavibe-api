from django.contrib import admin
from .models import Profile


# Register profile so it shows up in admin panel
admin.site.register(Profile)
