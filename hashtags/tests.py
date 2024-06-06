"""
Test Runner script for the Hashtags functionality in the 
Django REST application.

This script contains test cases for the Hashtag model and 
its related API endpoints. It ensures that Django is properly 
initialized & configured before executing the tests. 

The test cases are custom coded with inspiration from sources 
listed in the README chapter Credits, Content.
"""
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from hashtags.models import Hashtag
from posts.models import Post

class HashtagTests(APITestCase):
    """
    Test suite for the Hashtag model and API endpoints.
    """
    def setUp(self):
      """
      Set up the test environment.
      This method creates a test user and logs in the user.
      """
      # Create a test user and log in
      self.user = User.objects.create_user(
          username='testuser',
          password='testpassword')
      self.client.login(username='testuser', password='testpassword')

    def tearDown(self):
        """
        Tear down the test environment.

        This method logs out the test user and deletes all User, 
        Post, and Hashtag instances.
        """
        self.client.logout()
        User.objects.all().delete()
        Post.objects.all().delete()
        Hashtag.objects.all().delete()

    def test_create_hashtag(self):
        """
        Test the creation of a hashtag.

        - A user can create a hashtag.
        - The response contains the correct hashtag data, including the name
          of the created hashtag.
        - This test ensures that the API allows the creation of hashtags and
          that the returned data matches the expected structure.
        """
        url = reverse('hashtag-list')
        data = {'name': 'example'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'example')

    def test_create_post_with_hashtag(self):
        """
        Test the creation of a post with an associated hashtag.

        - A user can create a post with an associated hashtag.
        - Response contains correct post data, incl title of created post.
        - Response incl. hashtag_ids field with the ID of the assoc. hashtag
        - This test ensures that posts can be created with hashtags and
          verifies that the hashtag is correctly associated with the post by
          checking the hashtag_ids in the response.
        """
        hashtag = Hashtag.objects.create(name='example')
        url = reverse('post-list')
        data = {
            'title': 'Test Post',
            'content': 'This is a test post with a hashtag',
            'hashtag_ids': [hashtag.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Test Post')
        self.assertIn('hashtag_ids', response.data)
        self.assertEqual(response.data['hashtag_ids'][0], hashtag.id)

    def test_search_post_by_hashtag(self):
        """
        Test searching for a post by hashtag.

        - A post can be tagged with a hashtag.
        - The post can be retrieved by searching for that hashtag.
        - Response contains correct post data, incl. the assoc. hashtag ID.
        - This test ensures that the search functionality works correctly by
          retrieving posts associated with a specific hashtag and verifying
          that the returned post data includes the correct hashtag.
        """
        hashtag = Hashtag.objects.create(name='example')
        post = Post.objects.create(
            owner=self.user,
            title='Test Post',
            content='This is a test post with a hashtag'
        )
        post.hashtags.add(hashtag)
        url = reverse('post-list')
        response = self.client.get(url, {'search': 'example'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['title'], 'Test Post')
        self.assertIn(
            hashtag.id, response.data['results'][0]['hashtag_ids'])

    def test_add_remove_hashtag_to_post(self):
        """
        Test adding and removing a hashtag to/from a post.
        
        - A user can add a hashtag to a post.
        - Response reflects added hashtag in the 'hashtag' field.
        - A user can remove a hashtag from a post
        - Response correctly updates to reflect removal of the hashtag in the
          'hashtag' field.
        - This test ensures that hashtags can be dynamically added to and
          removed from posts and that these changes are accurately reflected
          in the response.
        """
        hashtag = Hashtag.objects.create(name='example')
        post = Post.objects.create(
            owner=self.user,
            title='Test Post',
            content='This is a test post with a hashtag'
        )
        post.hashtags.add(hashtag)
        url = reverse('post-detail', kwargs={'pk': post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(
            hashtag.id, [tag['id'] for tag in response.data['hashtags']]
        )
        post.hashtags.remove(hashtag)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotIn(
            hashtag.id, [tag['id'] for tag in response.data['hashtags']]
        )
