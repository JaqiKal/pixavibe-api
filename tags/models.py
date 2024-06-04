from django.db import models

class Tag(models.Model):
    """
    This model allows tagging of post with keywords.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
