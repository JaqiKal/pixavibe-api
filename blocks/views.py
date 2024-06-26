from rest_framework import generics, permissions
from .models import Block
from .serializers import BlockSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class BlockList(generics.ListCreateAPIView):
    """
    List of blocked users. If authenticated, create a block.
    """
    serializer_class = BlockSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Block.objects.all()

    def get_queryset(self):
        """
        This method returns a queryset of blocks for the currently
        authenticated user. If the user is not authenticated, it
        returns an empty queryset.
        """
        user = self.request.user
        if user.is_authenticated:
            return Block.objects.filter(owner=user)
        else:
            return Block.objects.none()

    def perform_create(self, serializer):
        """
        This method saves the new block instance with the owner
        set to the currently authenticated user.
        """
        serializer.save(owner=self.request.user)


class BlockDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a block,
    If you're the owner, also delete the block.
    """
    serializer_class = BlockSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Block.objects.all()
