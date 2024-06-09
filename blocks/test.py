from django.contrib.auth.models import User
from django.test import TransactionTestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import BlockUser

class BlockUserTests(TransactionTestCase):
    """
    Test suite for the BlockUser model and API endpoints.
    """
    reset_sequences = True  # Ensure primary keys are reset between tests

    def setUp(self):
        """
        Set up the test environment.
        This method creates two test users and logs in the first user.
        """
        self.user1 = User.objects.create_user(
            username='user1',
            password='password1'
        )
        self.user2 = User.objects.create_user(
            username='user2',
            password='password2'
        )
        self.client.login(username='user1', password='password1')

    def tearDown(self):
        """
        Tear down the test environment.
        This method logs out the test user and deletes all User and BlockUser instances.
        """
        self.client.logout()
        User.objects.all().delete()
        BlockUser.objects.all().delete()

    def test_create_block(self):
        """
        Test the creation of a block.
        """
        url = reverse('block-list')
        data = {'target': self.user2.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['target'], self.user2.id)

    def test_list_blocks(self):
        """
        Test listing of blocks.
        """
        BlockUser.objects.create(owner=self.user1, target=self.user2)
        response = self.client.get(reverse('block-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
    
    def test_retrieve_block(self):
        """
        Test retrieving a block.
        """
        block = BlockUser.objects.create(owner=self.user1, target=self.user2)
        url = reverse('block-detail', kwargs={'pk': block.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['target'], self.user2.id)

    def test_delete_block(self):
        """
        Test deleting a block.
        """
        block = BlockUser.objects.create(owner=self.user1, target=self.user2)
        url = reverse('block-detail', kwargs={'pk': block.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(BlockUser.objects.count(), 0)

    def test_block_duplicate(self):
        """
        Test that a duplicate block cannot be created.
        """
        BlockUser.objects.create(owner=self.user1, target=self.user2)
        url = reverse('block-list')
        data = {'target': self.user2.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('possible duplicate', response.data['detail'])

    def test_cannot_block_without_authentication(self):
        """
        Test that a user cannot block another user without authentication.
        """
        self.client.logout()
        url = reverse('block-list')
        data = {'target': self.user2.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)







