from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'published_date', 'isbn', 'page_count')  # Columns to display
    list_filter = ('author', 'published_date')  # Filters in the right sidebar
    search_fields = ('title', 'author', 'isbn')  # Search fields
    ordering = ('-published_date',)  # Default ordering (descending by published_date)
    readonly_fields = ('id',)  # Fields set as read-only


admin.site.register(Book, BookAdmin)