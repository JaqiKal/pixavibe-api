# Amended from walkthrough 'drf_api', customized to cater for 'Hashtags'.
# This module defines serializers for handling posts, including
# creating and updating posts with associated hashtags and images.
import re
from rest_framework import serializers
from posts.models import Post
from likes.models import Like
from hashtags.models import Hashtag
from hashtags.serializers import HashtagSerializer
from category.models import Category


# Serializer for serializing Post instances to JSON,
# focusing on read operations.
class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    hashtags = HashtagSerializer(many=True, read_only=True)
    category_name = serializers.ReadOnlyField(source='category.name')

    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name',
        allow_null=True,
        required=False
    )

    def validate_image(self, value):
        """
        Validates the image uploaded with the post,
        checking its size and dimensions.
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
        Determines if the current user is the owner of the post.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        """
        Retrieves the ID of the current user's like for the post, if any.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    def get_category_name(self, obj):
        """
        Retrieves the name of the category
        associated with the post, if any.
        """
        return obj.category.name if obj.category else None

    # Meta class for specifying the model & fields to serialize.
    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'image_filter',
            'like_id', 'likes_count', 'comments_count',
            'hashtags', 'category', 'category_name',
        ]


# Serializer for creating & updating Post instances,
# including associating hashtags via their IDs
class PostCreateUpdateSerializer(serializers.ModelSerializer):
    # Allows specifying hashtags by their IDs during
    # creation or update of a post.
    hashtag_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Hashtag.objects.all(),
        source='hashtags',
    )
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name',
        allow_null=True,
        required=False
    )

    # Meta class for specifying the model & fields to serialize.
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'content', 'image',
            'image_filter', 'hashtag_ids',
            'profile_image', 'category'
        ]

    def validate_hashtag_ids(self, value):
        """
        Validates the IDs of hashtags being associated with the post.
        """
        for hashtag in value:
            # Ensure the hashtag name does not exceed 30 characters
            if len(hashtag.name) > 30:
                raise serializers.ValidationError(
                    f"Hashtag '{hashtag.name}' is too long."
                )
                # Allow hashtags with letters, numbers, and underscores
            if not re.match(r'^[\w_]+$', str(hashtag.id)):
                raise serializers.ValidationError(
                    f"Hashtag '{hashtag.name}' contains invalid characters."
                )
        return value

    def create(self, validated_data):
        hashtags = validated_data.pop('hashtags')
        post = Post.objects.create(**validated_data)
        post.hashtags.set(hashtags)
        return post

    def update(self, instance, validated_data):
        hashtags = validated_data.pop('hashtags')
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.image = validated_data.get('image', instance.image)
        instance.image_filter = validated_data.get(
            'image_filter',
            instance.image_filter
        )
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        instance.hashtags.set(hashtags)
        return instance
