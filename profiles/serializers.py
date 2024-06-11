"""
Amended from walkthrough 'drf_api', customized to cater for 
blocking functionality.

Serializers for the Profile model to convert model instances to
JSON representations and vice versa. Handles custom fields for 
user ownership, following status, and blocking status.

"""
from rest_framework import serializers
from .models import Profile
from followers.models import Follower
from blocks.models import Block

class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model. Includes custom fields to handle
    user ownership, following status, and blocking status.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    blocking_id = serializers.SerializerMethodField()
    blocking_target = serializers.SerializerMethodField()
    is_blocking = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Checks if the request user is the owner of the profile.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        """
        Retrieves the ID of the following relationship if the user is 
        following the profile owner.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    def get_is_blocking(self, obj):
        """
        Checks if the request user is blocking the profile owner.
        
        Returns:
        - bool: True if the request user is blocking the profile owner,
          else False.
        """
        user = self.context['request'].user
        blocking = Block.objects.filter(owner=user, target=obj.owner).first()
        return blocking is not None

    def get_blocking_id(self, obj):
        """
        Retrieves the ID of the blocking relationship if the user is
        blocking the profile owner.
 
        Returns:
        - int or None: The ID of the blocking relationship or None if
          not blocking.
        """
        user = self.context['request'].user
        blocking = Block.objects.filter(owner=user, target=obj.owner).first()
        if blocking:
            return blocking.target.id
        return None

    def get_blocking_target(self, obj):
        """
        Retrieves the username of the target being blocked by the user.

        Returns:
        - str or None: The username of the target being blocked or 
          None if not blocking.
        """
        user = self.context['request'].user
        blocking = Block.objects.filter(owner=user, target=obj.owner).first()
        if blocking:
            return blocking.target.username
        return None
    
    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'content', 'image', 'is_owner', 'following_id',
            'blocking_id', 'blocking_target', 'is_blocking',
            'posts_count', 'followers_count', 'following_count',
        ]
