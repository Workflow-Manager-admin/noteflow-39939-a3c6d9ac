from django.contrib import admin
from .models import Note

# Register your models here.


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for Note model.
    """
    list_display = ('title', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-updated_at',)

    fieldsets = (
        (None, {
            'fields': ('title', 'content')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
