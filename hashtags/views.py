from rest_framework import viewsets, permissions
from .models import Hashtag
from .serializers import HashtagSerializer


class HashtagViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing hashtag instances.
    """
    serializer_class = HashtagSerializer
    queryset = Hashtag.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
