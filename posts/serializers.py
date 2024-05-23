from rest_framework import serializers
from posts.models import Post


class PostsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate_image(self, value):
        """
        Validates the image file size and height
        and sends a message if file is too large to upload
        """
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        """
        Determine if the requesting user is the owner of the profile.
        """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        # Specify the model to be serialized.
        model = Post
        # Define the fields to be included in the serialized representation. 
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image',  'image_filter'
        ]
