
from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


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
        User.objects.create_user(username='adam', password='pass')
        self.client.login(username='adam', password='pass')
        self.fail_case = True

    def tearDown(self):
        """
        Clean up after each test method to reset the environment.
        Logs out the user and deletes all User and Post instances.
        """
        self.client.logout()
        User.objects.all().delete()
        Post.objects.all().delete()

    def print_existing_users(self):
        """
        Print all existing users in the database.
        This method is useful for debugging purposes to see which users
        are present in the test database.
        """
        users = User.objects.all()
        for user in users:
            print(f"Existing user: {user.username}")

    @fail_first
    def test_can_list_posts(self):
        """
        Ensure that posts can be listed correctly and verify the
        response status.
        """
        Post.objects.create(
            owner=User.objects.get(username='adam'), title='a title'
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
        response = self.client.post('/posts/', {'title': 'a title'})
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
        self.adam = User.objects.create_user(
            username='adam',
            password='pass'
        )
        self.brian = User.objects.create_user(
            username='brian',
            password='pass'
        )
        Post.objects.create(
            owner=self.adam,
            title='a title',
            content='adams content'
        )
        Post.objects.create(
            owner=self.brian,
            title='another title',
            content='brians content'
        )
        self.client.login(username='adam', password='pass')
        self.fail_case = True

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
        response = self.client.put('/posts/1/', {'title': 'a new title'})
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
