from django.contrib.auth.models import User
from django.test import TransactionTestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Block
from posts.models import Post

class BlockTests(TransactionTestCase):
    """
    Test suite for the Block model and API endpoints.
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
        This method logs out the test user and deletes all User and Block instances.
        """
        self.client.logout()
        User.objects.all().delete()
        Block.objects.all().delete()

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
        Block.objects.create(owner=self.user1, target=self.user2)
        response = self.client.get(reverse('block-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
    
    def test_retrieve_block(self):
        """
        Test retrieving a block.
        """
        block = Block.objects.create(owner=self.user1, target=self.user2)
        url = reverse('block-detail', kwargs={'pk': block.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['target'], self.user2.id)

    def test_delete_block(self):
        """
        Test deleting a block.
        """
        block = Block.objects.create(owner=self.user1, target=self.user2)
        url = reverse('block-detail', kwargs={'pk': block.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Block.objects.count(), 0)

    def test_block_duplicate(self):
        """
        Test that a duplicate block cannot be created.
        """
        Block.objects.create(owner=self.user1, target=self.user2)
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

class BlockPostTests(APITestCase):
    """
    Test suite for blocking and unblocking users and the visibility of posts.
    """

    def setUp(self):
        """
        Set up necessary preconditions and initialize objects before each test.
        """
        self.user1 = User.objects.create_user(username='user1', password='password1')
        self.user2 = User.objects.create_user(username='user2', password='password2')
        self.client.login(username='user1', password='password1')
        self.post_by_user2 = Post.objects.create(owner=self.user2, title='Post by User 2', content='Content by user 2')
        self.post_by_user1 = Post.objects.create(owner=self.user1, title='Post by User 1', content='Content by user 1')

    def tearDown(self):
        """
        Clean up after each test method to reset the environment.
        """
        self.client.logout()
        User.objects.all().delete()
        Post.objects.all().delete()
        Block.objects.all().delete()

    def test_block_user(self):
        """
        Test that blocking a user hides their posts from the blocking user.
        """
        # Block user2
        url = reverse('block-list')
        data = {'target': self.user2.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Check that user1 cannot see posts by user2
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        post_titles = [post['title'] for post in response.data['results']]
        self.assertNotIn('Post by User 2', post_titles)

    def test_unblock_user(self):
        """
        Test that unblocking a user makes their posts visible to the unblocking user.
        """
        # Block and then unblock user2
        Block.objects.create(owner=self.user1, target=self.user2)
        block = Block.objects.get(owner=self.user1, target=self.user2)
        url = reverse('block-detail', kwargs={'pk': block.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Check that user1 can see posts by user2
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        post_titles = [post['title'] for post in response.data['results']]
        self.assertIn('Post by User 2', post_titles)

    def test_visibility_of_own_posts(self):
        """
        Test that users can always see their own posts regardless of blocks.
        """
        # Block user1's own post to check self-visibility
        Block.objects.create(owner=self.user1, target=self.user2)
        
        # Check that user1 can still see their own post
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        post_titles = [post['title'] for post in response.data['results']]
        self.assertIn('Post by User 1', post_titles)

    def test_block_without_authentication(self):
        """
        Test that blocking another user without authentication is not allowed.
        """
        self.client.logout()
        url = reverse('block-list')
        data = {'target': self.user2.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_visibility_after_block_and_unblock(self):
        """
        Test that posts from a blocked user are hidden and then shown after unblocking.
        """
        # Block user2
        Block.objects.create(owner=self.user1, target=self.user2)
        
        # Check that user1 cannot see posts by user2
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        post_titles = [post['title'] for post in response.data['results']]
        self.assertNotIn('Post by User 2', post_titles)

        # Unblock user2
        block = Block.objects.get(owner=self.user1, target=self.user2)
        url = reverse('block-detail', kwargs={'pk': block.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Check that user1 can see posts by user2 again
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        post_titles = [post['title'] for post in response.data['results']]
        self.assertIn('Post by User 2', post_titles)