from rest_framework import serializers
from .models import Note


# PUBLIC_INTERFACE
class NoteSerializer(serializers.ModelSerializer):
    """
    Serializer for Note model providing CRUD operations.

    This serializer handles the conversion between Note model instances
    and JSON representation for API requests and responses.

    Fields:
        id: Auto-generated primary key (read-only)
        title: Note title (required, max 200 characters)
        content: Note content (required)
        created_at: Creation timestamp (read-only)
        updated_at: Last update timestamp (read-only)
    """

    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_title(self, value):
        """
        Validate that title is not empty after stripping whitespace.
        """
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value.strip()

    def validate_content(self, value):
        """
        Validate that content is not empty after stripping whitespace.
        """
        if not value.strip():
            raise serializers.ValidationError("Content cannot be empty.")
        return value.strip()
