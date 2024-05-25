from rest_framework import serializers
from .models import Likes


class LikesSerializer(serializers.ModelSerializer):
    """
    Serializer for the Likes model
    Adds three extra fields when returning a list of Comment instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    post = serializers.ReadOnlyField(source='owner.profile.id')
    created_at= serializers.DateTimeField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'post', 'created_at'
        ]
