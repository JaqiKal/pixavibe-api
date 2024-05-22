from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../pixavibe/default_profile_pbhpua.jpg'
    )
    # Return instances in reverse order
    class Meta:
        ordering = ['-created_at']

    # human-readable string with info of who owner is
    def __str__(self):
        return f"{self.owner}'s profile"

# Define create profile function before passing it as an argument
def create_profile(sender, instance, created, **kwargs):
    """
    Define create profile function before passing it as an argument
    """
    if created:
        Profile.objects.create(owner=instance)

# Listen for the post_save signal coming from the User model
# by calling the connect function
post_save.connect(create_profile, sender=User)