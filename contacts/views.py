# Customized to cater for contact management functionality. This module
# defines the views for the Contact model. It includes views for listing
# and creating contacts, as well as retrieving, updating, and deleting
# individual contact instances.

from rest_framework import generics, permissions
from .models import Contact
from .serializers import ContactSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class ContactList(generics.ListCreateAPIView):
    """
    List contacts or create a contact if logged in.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Saves the new contact instance with the owner set to the current user.
        """
        serializer.save(owner=self.request.user)


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting a contact.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsOwnerOrReadOnly]
