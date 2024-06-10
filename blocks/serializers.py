from rest_framework import serializers
from django.db import IntegrityError
from .models import BlockUser


class BlockUserSerializer(serializers.ModelSerializer):
    """
    Serializer for the Block model.'owner' initiates block and 'target' is 
    the blocked user.The 'owner' and 'target_username' fields are read-only, 
    ensuring that they are populated from the related User model and not 
    from user input.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = BlockUser
        fields = ['id', 'owner', 'target', 'created_at', 'target_username']

    def create(self, validated_data):
        """
        Create a new Block instance.
        This method overrides the default create method to handle
        IntegrityError, which occurs when a duplicate block is attempted.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                {'detail': 'possible duplicate'}
            )
