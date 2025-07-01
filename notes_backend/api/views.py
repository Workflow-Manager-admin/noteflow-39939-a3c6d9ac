from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Note
from .serializers import NoteSerializer


# PUBLIC_INTERFACE
@api_view(['GET'])
def health(request):
    """
    Health check endpoint to verify server status.
    """
    return Response({"message": "Server is up!"})


# PUBLIC_INTERFACE
class NoteListCreateAPIView(generics.ListCreateAPIView):
    """
    API view for listing all notes and creating new notes.

    GET /api/notes/ - Returns a list of all notes ordered by most recently updated
    POST /api/notes/ - Creates a new note
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    @swagger_auto_schema(
        operation_summary="List all notes",
        operation_description="Retrieve a list of all notes ordered by most recently updated first",
        responses={
            200: openapi.Response(
                description="List of notes retrieved successfully",
                schema=NoteSerializer(many=True)
            )
        },
        tags=['notes']
    )
    def get(self, request, *args, **kwargs):
        """List all notes."""
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new note",
        operation_description="Create a new note with title and content",
        request_body=NoteSerializer,
        responses={
            201: openapi.Response(
                description="Note created successfully",
                schema=NoteSerializer()
            ),
            400: openapi.Response(
                description="Invalid input data"
            )
        },
        tags=['notes']
    )
    def post(self, request, *args, **kwargs):
        """Create a new note."""
        return super().post(request, *args, **kwargs)


# PUBLIC_INTERFACE
class NoteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a specific note.

    GET /api/notes/{id}/ - Retrieve a specific note
    PUT /api/notes/{id}/ - Update a specific note (full update)
    PATCH /api/notes/{id}/ - Partially update a specific note
    DELETE /api/notes/{id}/ - Delete a specific note
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    @swagger_auto_schema(
        operation_summary="Retrieve a note",
        operation_description="Retrieve a specific note by its ID",
        responses={
            200: openapi.Response(
                description="Note retrieved successfully",
                schema=NoteSerializer()
            ),
            404: openapi.Response(
                description="Note not found"
            )
        },
        tags=['notes']
    )
    def get(self, request, *args, **kwargs):
        """Retrieve a specific note."""
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a note",
        operation_description="Update all fields of a specific note",
        request_body=NoteSerializer,
        responses={
            200: openapi.Response(
                description="Note updated successfully",
                schema=NoteSerializer()
            ),
            400: openapi.Response(
                description="Invalid input data"
            ),
            404: openapi.Response(
                description="Note not found"
            )
        },
        tags=['notes']
    )
    def put(self, request, *args, **kwargs):
        """Update a specific note (full update)."""
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partially update a note",
        operation_description="Update specific fields of a note",
        request_body=NoteSerializer,
        responses={
            200: openapi.Response(
                description="Note updated successfully",
                schema=NoteSerializer()
            ),
            400: openapi.Response(
                description="Invalid input data"
            ),
            404: openapi.Response(
                description="Note not found"
            )
        },
        tags=['notes']
    )
    def patch(self, request, *args, **kwargs):
        """Partially update a specific note."""
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a note",
        operation_description="Delete a specific note by its ID",
        responses={
            204: openapi.Response(
                description="Note deleted successfully"
            ),
            404: openapi.Response(
                description="Note not found"
            )
        },
        tags=['notes']
    )
    def delete(self, request, *args, **kwargs):
        """Delete a specific note."""
        return super().delete(request, *args, **kwargs)
