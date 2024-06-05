# Customized to cater for contact management functionality.
# This module defines the serializer for the Contact model. 
# The serializer converts the Contact model instances to 
# JSON format and validates the data.

from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer for the Contact model. 
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")

    class Meta:
        """
        Meta class to define the model and fields to be serialized.
        """
        model = Contact
        fields = [
            'id', 
            'owner',
            'reason',
            'content',
            "profile_id",
            "profile_image",
            'created_at',
            'updated_at',
        ]