from django.db import models
from django.contrib.auth.models import User

class BlockUser(models.Model):
    """
    Block model creates a relationship between the user who initiates
    the block (owner) and the user being blocked (target). A user can
    block another user, preventing the blocked user from interacting
    with the blocker's content.
    """
    owner = models.ForeignKey(
        User, related_name='blocking', on_delete=models.CASCADE
    )
    target = models.ForeignKey(
        User,
        related_name='blocked_by', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Order blocks by time of creation
        ordering = ['-created_at']
        # Ensures that the same user cannot block another user more than once
        unique_together = ['owner', 'target']

    def __str__(self):
        return f'{self.owner} {self.target}'



