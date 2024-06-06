"""
Test Runner script for the Likes functionality in the Django REST application.

This script contains test cases for the Like model and its related
API endpoints. It ensures that Django is properly initialized & configured
before executing the tests.

The test cases are custom coded with inspiration from sources listed
in the README chapter Credits, Content.
"""
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from likes.models import Like
from posts.models import Post
from django.db import transaction


class LikeTests(APITestCase):
    """
    Test suite for the Like model and API endpoints.
    """
    def setUp(self):
        """
        Set up the test environment.
        This method creates a test user and a test post.
        """
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.post = Post.objects.create(
            owner=self.user, title='Test Post', content='Test Content'
        )
        self.client.login(
            username='testuser', password='testpassword'
        )

    def tearDown(self):
        """
        Tear down the test environment.
        This method logs out the test user and deletes
        all User, Post, and Like instances.
        """
        self.client.logout()
        User.objects.all().delete()
        Post.objects.all().delete()
        Like.objects.all().delete()

    def test_like_post(self):
        """
        Test that a user can like a post and verify the response status.
        """
        url = reverse('like-list')
        data = {'post': self.post.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['post'], self.post.id)

    def test_cannot_like_post_twice(self):
        """
        Ensure that a user cannot like a post twice and receives
        a validation error.

        Amended with help of:
        https://www.geeksforgeeks.org/transaction-atomic-with-django/
        Ensures the operations within this block are treated as a single unit,
        allowing for a rollback if any issue occurs to maintain data integrity.
        """
        Like.objects.create(owner=self.user, post=self.post)
        url = reverse('like-list')
        data = {'post': self.post.id}

        with transaction.atomic():
            response = self.client.post(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn('detail', response.data)

    def test_unlike_post(self):
        """
        Test that a user can unlike a post and verify the response status.

        Amended with help of:
        https://www.geeksforgeeks.org/transaction-atomic-with-django/
        Ensures the operations within this block are treated as a single unit,
        allowing for a rollback if any issue occurs to maintain data integrity.
        """
        like = Like.objects.create(owner=self.user, post=self.post)
        url = reverse('like-detail', kwargs={'pk': like.id})

        with transaction.atomic():
            response = self.client.delete(url)
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_unlike_another_users_like(self):
        """
        Ensure that a user cannot unlike another user's like and receives
        the appropriate forbidden response.

        Amended with help of:
        https://www.geeksforgeeks.org/transaction-atomic-with-django/
        Ensures the operations within this block are treated as a single unit,
        allowing for a rollback if any issue occurs to maintain data integrity.
        """
        another_user = User.objects.create_user(
            username='anotheruser',
            password='anotherpassword'
        )
        like = Like.objects.create(owner=another_user, post=self.post)
        url = reverse('like-detail', kwargs={'pk': like.id})

        with transaction.atomic():
            response = self.client.delete(url)
            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
