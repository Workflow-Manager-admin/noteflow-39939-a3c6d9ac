from django.db import models


# PUBLIC_INTERFACE
class Note(models.Model):
    """
    Note model for storing user notes with title, content, and timestamps.

    Fields:
        id: Primary key (auto-generated)
        title: Note title (max 200 characters)
        content: Note content (text field for longer content)
        created_at: Timestamp when note was created (auto-set on creation)
        updated_at: Timestamp when note was last updated (auto-set on update)
    """
    title = models.CharField(max_length=200, help_text="Title of the note")
    content = models.TextField(help_text="Main content of the note")
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the note was created"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Timestamp when the note was last updated"
    )

    class Meta:
        ordering = ['-updated_at']  # Order by most recently updated first
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self):
        return self.title
