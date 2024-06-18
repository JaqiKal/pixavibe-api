from django.db import models


class Hashtag(models.Model):
    """
    This model allows tagging of posts with hashtags.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
