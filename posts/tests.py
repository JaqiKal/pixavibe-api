from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    """
    Test suite for the PostListView API endpoint.
    """
    def setUp(self):
        """
        Set up the test environment.
        This method is called before each test to set up any state
        that is shared among the tests. Here, it creates a user
        named 'adam' with a password 'pass'.
        """
        User.objects.create_user(username='adam', password='pass')

    def test_can_list_posts(self):
        """
        Test the ability to list posts.
        This method tests if the API endpoint for listing posts is working
        correctly by creating a post and verifying that it can be retrieved
        successfully.
        """
        adam = User.objects.get(username='adam')
        Post.objects.create(owner=adam, title='a title')
        response = self.client.get('/posts/')

        # This assertion is used to illustrate a failing test case.
        # AssertionError: 200 != 201
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # This is the correct assertion for the test case, ensuring that
        # the response status code is 200 OK, indicating that the request
        # was successful and posts can be listed.
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        """
        Test that a logged-in user can create a post.

        This method tests if an authenticated user can successfully
        create a post using the API endpoint.
        """
        self.client.login(username='adam', password='pass')
        response = self.client.post('/posts/', {'title': 'a title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        # This assertion is used to illustrate a failing test case.
        # AssertionError: 201 != 200
        # self.assertEqual(response.status_code, status.HTTP_200_OK)

        # This is the correct assertion for the test case, ensuring that
        # the response status code is 201 Created, indicating that the
        # post was successfully created.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_post(self):
        """
        Test that a user who is not logged in cannot create a post.
        This method tests if an unauthenticated user is prevented from
        creating a post using the API endpoint.
        """
        response = self.client.post('/posts/', {'title': 'a title'})

        # This assertion is used to illustrate a failing test case
        # It is intentionally incorrect to demonstrate what happens
        # when the expected status code does not match the actual status code
        # AssertionError: 403 != 200
        # self.assertEqual(response.status_code, status.HTTP_200_OK)

        # This is the correct assertion for the test case
        # Ensuring that the response status code is 403 Forbidden,
        # indicating that the user is not authorized to create a post
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    """
    Test suite for the PostDetailView API endpoint.
    """
    def setUp(self):
        """
        Set up the test environment.
        This method is called before each test to set up any state that is
        shared among the tests. Here, it creates two users, 'adam' and 'brian',
        and creates a post for each user.
        """
        adam = User.objects.create_user(username='adam', password='pass')
        brian = User.objects.create_user(username='brian', password='pass')

        Post.objects.create(
            owner=adam, title='a title', content='adams content'
        )

        Post.objects.create(
            owner=brian, title='another title', content='brians content'
        )

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'a title')

        # Make test fail by,
        # #self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Send correct assertation
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        response = self.client.get('/posts/999/')

        # Make test fail by,
        # self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Send correct assertation
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put('/posts/1/', {'title': 'a new title'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'a new title')
        # Make test fail by,
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Send correct assertation
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_post(self):
        """
        As the last challenge, I’d like to ask you to login as one
        of the users. Then, send a put request to post/id, with
        the ID of the post that the other user owns.
        """
        self.client.login(username='adam', password='pass')
        response = self.client.put('/posts/2/', {'title': 'a new title'})
        # Make test fail by,
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Send correct assertation
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
