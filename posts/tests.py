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
