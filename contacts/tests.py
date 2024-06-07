from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from .models import Contact
from .serializers import ContactSerializer


# Test cases for serializer validation
class ContactSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        self.valid_data = {
            'reason': 'Test Reason',
            'content': 'Test content of the contact.',
            'owner': self.user
        }
        self.invalid_data_reason = {
            'reason': '   ',  # Invalid reason (only spaces)
            'content': 'Test content of the contact.',
            'owner': self.user
        }
        self.invalid_data_content = {
            'reason': 'Test Reason',
            'content': '   ',  # Invalid content (only spaces),
            'owner': self.user
        }

    def tearDown(self):
        User.objects.all().delete()
        Contact.objects.all().delete()

    def test_valid_contact_serializer(self):
        """
        Ensures the serializer accepts valid data.
        """
        serializer = ContactSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_contact_serializer_reason(self):
        """
        Ensures the serializer rejects invalid reason data.
        """
        serializer = ContactSerializer(data=self.invalid_data_reason)
        self.assertFalse(serializer.is_valid())
        self.assertIn('reason', serializer.errors)

    def test_invalid_contact_serializer_content(self):
        """
        Ensures the serializer rejects invalid content data.
        """
        serializer = ContactSerializer(data=self.invalid_data_content)
        self.assertFalse(serializer.is_valid())
        self.assertIn('content', serializer.errors)


# Test cases for API validation
class ContactAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        self.client.login(
            username='testuser', password='testpass'
        )
        self.valid_data = {
            'reason': 'Test Reason',
            'content': 'Test content of the contact.',
            'owner': self.user
        }
        self.invalid_data_reason = {
            'reason': '   ',  # Invalid reason (only spaces)
            'content': 'Test content of the contact.',
            'owner': self.user
        }
        self.invalid_data_content = {
            'reason': 'Test Reason',
            'content': '   ',  # Invalid content (only spaces),
            'owner': self.user
        }

        self.contacts_url = reverse('contact-list')

    def tearDown(self):
        self.client.logout()
        User.objects.all().delete()
        Contact.objects.all().delete()

    def test_create_contact_valid(self):
        """
        Ensures the API creates a contact with valid data.
        """
        response = self.client.post(self.contacts_url, self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_contact_invalid_reason(self):
        """
        Ensures the API responds with a 400 Bad Request status and
        the appropriate error when reason is invalid.
        """
        response = self.client.post(
            self.contacts_url, self.invalid_data_reason
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('reason', response.data)

    def test_create_contact_invalid_content(self):
        """
        Ensures the API responds with a 400 Bad Request status
        and the appropriate error when content is invalid.
        """
        response = self.client.post(
            self.contacts_url, self.invalid_data_content
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('content', response.data)

    def test_create_contact_unauthenticated(self):
        """
        Ensures the API prevents unauthenticated users from creating contacts.
        """
        self.client.logout()
        response = self.client.post(self.contacts_url, self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
