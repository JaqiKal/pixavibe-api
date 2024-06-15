from rest_framework import generics, permissions
from .models import Category
from .serializers import CategorySerializer, CategoryDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly


class CategoryList(generics.ListAPIView):
    """
    API view to list all categories.
    Allows filtering by name.
    """    
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a category by id.
    Only the owner can update or delete.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()





