from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class PostList(APIView):
    """
    List all posts or create a new post.
    """
    serializer_class = PostSerializer
    # Define the permission classes for this view
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        """
        Handle GET request to list all posts.
        """
        posts = Post.objects.all()
        serializer = PostSerializer(
            posts, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        """
        Handle POST request to create a new post.
        """
        # Deserialize the incoming data
        serializer = PostSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            # Save the new post with the owner set to the current user
            serializer.save(owner=request.user)
            # Return the serialized data with a 201 Created status
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        # Return validation errors with a 400 Bad Request status
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class PostDetail(APIView):
    """
    Retrieve a post and edit or delete it if you own it
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer

    def get_object(self, pk):
        """
        Retrieve a post by its primary key (pk).
        """
        try:
            # Attempt to retrieve the post from the database
            post = Post.objects.get(pk=pk)
            self.check_object_permissions(self.request, post)
            return post
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Handle GET request for retrieving a specific post.
        """
        post = self.get_object(pk)
        # Serialize the post data
        serializer = PostSerializer(
            post, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        
        """
        Handle PUT request for updating a specific post.
        """
        post = self.get_object(pk)
        # Deserialize the incoming data
        serializer = PostSerializer(
            post, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        """
        Handle DELETE request for deleting a specific post.
        """
        post = self.get_object(pk)
        post.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

    