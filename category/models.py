from django.db import models


class Category(models.Model):
    """
    Represents a category within an application.
    This model allows categorizing of posts.
    """
    name = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
