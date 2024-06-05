# Customized to cater for contact management functionality.
# This module defines the Contact model used to store information about 
# contacts made by users. It includes fields for the contact owner, reason, 
# content, and timestamps for creation and updates.

from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    """
    Represents a contact entry created by a user. 
    Each contact has an owner, reason, content, 
    and timestamps for creation and last update.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        """
        Returns a string representation of the contact, combining 
        the owner's username and the reason for the contact.
        """
        return f'{self.owner} : {self.reason}'
