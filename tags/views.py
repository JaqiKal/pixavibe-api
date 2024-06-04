from rest_framework import viewsets, permissions
from .models import Tag
from .serializers import TagSerializer

class TagViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing tag instances.
    """
    serializer_class= TagSerializer
    queryset = Tag.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

