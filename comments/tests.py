"""
Test Runner script for the Comments functionality in the 
Django REST application.

This script contains test cases for the Comment model and 
its related API endpoints. It ensures that Django is properly 
initialized & configured before executing the tests. 

The test cases are custom coded with inspiration from sources 
listed in the README chapter Credits, Content.
"""
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Comment
from posts.models import Post


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
                # Run the test again in passing mode
                test_func(*args, **kwargs)
                return
            raise AssertionError("Expected test to fail but it passed.")
        else:
            test_func(*args, **kwargs)
    return wrapper


class CommentTests(APITestCase):
    """
    Test suite for the Comment model and API endpoints.
    """
    def setUp(self):
        """
        Set up the test environment.
        """
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        self.post = Post.objects.create(owner=self.user, title='Test Post')
        self.comment_data = {'content': 'Test Comment', 'post': self.post.id}
        self.fail_case = True

    def tearDown(self):
        """
        Tear down the test environment.Logs out the test user and
        deletes all User, Post, and Comment instances.
        """
        self.client.logout()
        User.objects.all().delete()
        Post.objects.all().delete()
        Comment.objects.all().delete()

    @fail_first
    def test_can_list_comments(self):
        """
        Test the ability to list comments.
        """
        Comment.objects.create(
            content='Test Comment',
            post=self.post, owner=self.user
        )
        response = self.client.get('/comments/')

        # Print response for debugging
        print(response.status_code)
        print(response.data)

        if self.fail_case:
            # Make test fail by asserting an incorrect status code
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        else:
            # Send correct assertion
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    @fail_first
    def test_can_create_comment(self):
        """
        Test the ability to create a comment.
        """
        response = self.client.post(
            '/comments/',
            self.comment_data, format='json'
        )

        print(response.status_code)
        print(response.data)

        if self.fail_case:
            self.assertEqual(response.status_code, status.HTTP_200_OK)
        else:
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    @fail_first
    def test_can_retrieve_comment_using_valid_id(self):
        """
        Test the ability to retrieve a comment using a valid ID.
        """
        comment = Comment.objects.create(
            content='Test Comment',
            post=self.post,
            owner=self.user
        )
        response = self.client.get(f'/comments/{comment.id}/')
        print(response.status_code)
        print(response.data)

        if self.fail_case:
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        else:
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    @fail_first
    def test_cant_retrieve_comment_using_invalid_id(self):
        """
        Test that retrieving a comment with an invalid ID returns 404.
        """
        response = self.client.get('/comments/999/')

        if self.fail_case:
            self.assertEqual(response.status_code, status.HTTP_200_OK)
        else:
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    @fail_first
    def test_user_can_update_own_comment(self):
        comment = Comment.objects.create(
            content='Test Comment',
            post=self.post, owner=self.user
        )
        updated_data = {'content': 'Updated Comment', 'post': self.post.id}
        response = self.client.put(
            f'/comments/{comment.id}/',
            updated_data,
            format='json'
        )

        # Print response for debugging
        print(response.status_code)
        print(response.data)

        updated_comment = Comment.objects.get(id=comment.id)

        if self.fail_case:
            # Make test fail by asserting an incorrect status code
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        else:
            # Correct assertion
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(updated_comment.content, 'Updated Comment')

    @fail_first
    def test_user_can_delete_own_comment(self):
        """
        Test the ability to delete a comment.
        """
        comment = Comment.objects.create(
            content='Test Comment',
            post=self.post,
            owner=self.user
        )
        response = self.client.delete(f'/comments/{comment.id}/')

        print(response.status_code)
        print(response.data)

        if self.fail_case:
            self.assertEqual(response.status_code, status.HTTP_200_OK)
        else:
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    @fail_first
    def test_user_cant_create_comment_without_authentication(self):
        """
        Test that a user cannot create a comment without authentication.
        """
        self.client.logout()
        response = self.client.post(
            '/comments/',
            self.comment_data, format='json'
        )

        print(response.status_code)
        print(response.data)

        if self.fail_case:
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        else:
            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


if __name__ == "__main__":
    unittest.main()
