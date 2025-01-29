from rest_framework import generics
from .models import Book
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import BookSerializer

# List and Create View
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # Or [AllowAny] for testing


# Retrieve, Update, and Destroy View
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # Or [AllowAny] for testing

