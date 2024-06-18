from django.db import models
from django.contrib.auth.models import User
from hashtags.models import Hashtag
from category.models import Category


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    image_filter_choices = [
        ('1977', '1977'),
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'),
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'),
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'),
        ('normal', 'Normal'),
        ('nashville', 'Nashville'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'),
        ('valencia', 'Valencia'),
        ('walden', 'Walden'),
        ('xpro2', 'X-pro II')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='../pixavibe/default_profile_pbhpua.jpg',
        blank=True
    )
    image_filter = models.CharField(
        max_length=32,
        choices=image_filter_choices,
        default='normal'
    )
    hashtags = models.ManyToManyField(Hashtag, related_name='posts')
    category = models.ForeignKey(Category, null=True, blank=True,
                                 on_delete=models.SET_NULL)

    # Order posts by time of posting, starting with the most recent
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
