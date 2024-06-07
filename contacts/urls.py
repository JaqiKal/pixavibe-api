
# Customized to cater for contact management functionality. This module
# defines the URL patterns for the Contact app. It includes paths for
# listing, creating, retrieving, updating, and deleting contacts.

from django.urls import path
from .views import ContactList, ContactDetail

urlpatterns = [
    path('contacts/', ContactList.as_view(), name='contact-list'),
    path('contacts/<int:pk>/', ContactDetail.as_view(), name='contact-detail')
]