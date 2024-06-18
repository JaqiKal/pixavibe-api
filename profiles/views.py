"""
Amended from walkthrough 'drf_api', customized to cater for
blocking functionality.

This module defines API views for listing and retrieving
profile instances. Profiles include information about the
number of posts, followers, following, and blocking relationships.

"""
from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Profile
from .serializers import ProfileSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    Annotations:
    - posts_count: Number of posts created by the profile owner.
    - followers_count: Number of users following the profile owner.
    - following_count: Number of users the profile owner is following.
    - blocked_count: Number of users who have blocked the profile owner.
    - blocking_count: Number of users the profile owner has blocked
    """
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
        blocked_count=Count('owner__blocked_by', distinct=True),
        blocking_count=Count('owner__blocking', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile',
        'owner__blocked_by__target__profile',
        'owner__blocking__owner__profile',

    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'blocked_count',
        'blocking_count',
        'owner__following__created_at',
        'owner__followed__created_at',
        'owner__blocked__created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve, update or delete a profile if you are the owner.
    Annotations:
    - posts_count: Number of posts created by the profile owner.
    - followers_count: Number of users following the profile owner.
    - following_count: Number of users the profile owner is following.
    - blocked_count: Number of users who have blocked the profile owner.
    - blocking_count: Number of users the profile owner has blocked.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
            posts_count=Count('owner__post', distinct=True),
            followers_count=Count('owner__followed', distinct=True),
            following_count=Count('owner__following', distinct=True),
            blocked_count=Count('owner__blocked_by', distinct=True),
            blocking_count=Count('owner__blocking', distinct=True)
        ).order_by('-created_at')
    serializer_class = ProfileSerializer
