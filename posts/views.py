from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Post, Category
from .serializers import PostSerializer, PostCreateUpdateSerializer

class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
        'hashtags__name',
        'category',
    ]
    search_fields = [
        'owner__username',
        'title',
        'hashtags__name',
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]

    def get_queryset(self):
        queryset = Post.objects.annotate(
            likes_count=Count('likes', distinct=True),
            comments_count=Count('comment', distinct=True)
        ).order_by('-created_at')

        user = self.request.user
        if user.is_authenticated:
            blocked_users = user.blocking.values_list('target', flat=True)
            queryset = queryset.exclude(owner__in=blocked_users)
        return queryset

    def perform_create(self, serializer):
        """
        Create new post.
        """
        category_name = self.request.data.get('category', None)
        if category_name:
            category = Category.objects.get(name=category_name)
            serializer.save(owner=self.request.user, category=category)
        else:
            serializer.save(owner=self.request.user)
            
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = Post.objects.annotate(
            likes_count=Count('likes', distinct=True),
            comments_count=Count('comment', distinct=True)
        ).order_by('-created_at')

        user = self.request.user
        if user.is_authenticated:
            blocked_users = user.blocking.values_list('target', flat=True)
            queryset = queryset.exclude(owner__in=blocked_users)
        return queryset

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return PostCreateUpdateSerializer
        return PostSerializer

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)