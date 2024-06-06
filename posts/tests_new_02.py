from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from posts.models import Post
from hashtags.models import Hashtag


def fail_first(test_func):
    """
    A decorator that forces a test to fail at its first run with a
    deliberately wrong assertion to check error handling, then reruns
    the test with correct conditions to ensure it passes.
    """
    def wrapper(*args, **kwargs):
        test_case = args[0]
        if getattr(test_case, 'fail_case', True):
            try:
                test_func(*args, **kwargs)
            except AssertionError as e:
                print(f"Intentional fail: {e}")
                test_case.fail_case = False
                test_func(*args, **kwargs)  # Run test again in passing mode
                return
            raise AssertionError("Expected test to fail but it passed.")
        else:
            test_func(*args, **kwargs)
    return wrapper


class PostListViewTests(APITestCase):
    """
    Tests related to listing posts and interactions from a
    list view perspective within the Post app.
    """
    def setUp(self):
        """
        Set up necessary preconditions and initialize objects before
        each test is run. Creates a user and logs them in.
        """
        User.objects.create_user(username='albin', password='albinsson1')
        self.client.login(username='albin', password='albinsson1')
        self.fail_case = True

    def tearDown(self):
        """
        Clean up after each test method to reset the environment.
        Logs out the user and deletes all User and Post instances.
        """
        self.client.logout()
        User.objects.all().delete()
        Post.objects.all().delete()

    @fail_first
    def test_can_list_posts(self):
        """
        Ensure that posts can be listed correctly and verify the
        response status.
        """
        Post.objects.create(
            owner=User.objects.get(username='albin'), title='a title'
        )
        response = self.client.get('/posts/')
        if self.fail_case:
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        else:
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    @fail_first
    def test_logged_in_user_can_create_post(self):
        """
        Test that a logged-in user can create a post successfully and
        verify the response status.
        """
        url = reverse('post-list')
        data = {
            'title': 'A title',
            'content': 'Some content',
            'hashtag_ids': []
        }
        response = self.client.post(url, data, format='json')
        if self.fail_case:
            self.assertEqual(response.status_code, status.HTTP_200_OK)
        else:
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    @fail_first
    def test_user_not_logged_in_cant_create_post(self):
        """
        Ensure that an unauthenticated user cannot create a post
        and receives the appropriate forbidden response.
        """
        self.client.logout()
        response = self.client.post('/posts/', {'title': 'a title'})
        if self.fail_case:
            self.assertEqual(response.status_code, status.HTTP_200_OK)
        else:
            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    """
    Tests focused on the retrieval, update, and deletion of individual
    posts through the Post detail view.
    """
    def setUp(self):
        self.albin = User.objects.create_user(
            username='albin',
            password='albinsson1'
        )
        self.brian = User.objects.create_user(
            username='brian',
            password='briansson'
        )
        Post.objects.create(
            owner=self.albin,
            title='a title',
            content='albins content'
        )
        Post.objects.create(
            owner=self.brian,
            title='another title',
            content='brians content'
        )
        self.client.login(username='albin', password='albinsson1')
        self.fail_case = True

    def tearDown(self):
        """
        Clean up after each test method to reset the environment.
        Logs out the user and deletes all User and Post instances.
        """
        self.client.logout()
        User.objects.all().delete()
        Post.objects.all().delete()

    @fail_first
    def test_can_retrieve_post_using_valid_id(self):
        """
        Verify that a post can be retrieved using a valid ID and check
        the corresponding success response status.
        """
        response = self.client.get('/posts/1/')
        if self.fail_case:
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        else:
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    @fail_first
    def test_cant_retrieve_post_using_invalid_id(self):
        """
        Ensure that attempting to retrieve a post using an invalid ID '
        results in a 404 Not Found status.
        """
        response = self.client.get('/posts/999/')
        if self.fail_case:
            self.assertEqual(response.status_code, status.HTTP_200_OK)
        else:
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    @fail_first
    def test_user_can_update_own_post(self):
        """
        Test that a logged-in user can update their own post and validate
        changes with the correct response status.
        """
        post = Post.objects.create(
            owner=self.albin,
            title='Original title',
            content='Original content'
        )
        url = reverse('post-detail', kwargs={'pk': post.id})
        data = {
            'title': 'Updated title',
            'content': 'Updated content',
            'hashtag_ids': []
        }
        response = self.client.put(url, data, format='json')
        if self.fail_case:
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        else:
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    @fail_first
    def test_user_cant_update_another_users_post(self):
        """
        Confirm that a user cannot update another user's post and
        receives the correct forbidden response status.
        """
        response = self.client.put('/posts/2/', {'title': 'a new title'})
        if self.fail_case:
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        else:
            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class PostDeletionTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.other_user = User.objects.create_user(
            username='otheruser', password='otherpassword')
        self.client.login(username='testuser', password='testpassword')
        self.post = Post.objects.create(
            owner=self.user, title='A title', content='Some content')

    def tearDown(self):
        self.client.logout()
        User.objects.all().delete()
        Post.objects.all().delete()

    def test_user_can_delete_own_post(self):
        url = reverse('post-detail', kwargs={'pk': self.post.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_delete_another_users_post(self):
        self.client.logout()
        self.client.login(username='otheruser', password='otherpassword')
        url = reverse('post-detail', kwargs={'pk': self.post.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)





class HashtagTests(APITestCase):
    def setUp(self):
        # Create a test user and log in
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def tearDown(self):
        self.client.logout()
        User.objects.all().delete()
        Post.objects.all().delete()
        Hashtag.objects.all().delete()

    def test_create_hashtag(self):
        """
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




if __name__ == '__main__':
    from django.test.utils import get_runner
    from django.conf import settings
    import sys

    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(['posts.tests_new_02'])
    sys.exit(bool(failures))
