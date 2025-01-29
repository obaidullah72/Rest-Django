from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Item, Location
from .serializers import ItemSerializers, LocationSerializers


class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializers
    permission_classes = [AllowAny]  # Or [AllowAny] for testing
    queryset = Item.objects.all()
    def get_queryset(self):
        queryset = Item.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(location=location)
        return queryset
    
    
class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializers
    queryset = Item.objects.all()
    permission_classes = [AllowAny]  # Or [AllowAny] for testing

    
    
class LocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializers
    queryset = Location.objects.all()
    permission_classes = [AllowAny]  # Or [AllowAny] for testing
    
    
    
class LocationDetail(generics.ListCreateAPIView):
    serializer_class = LocationSerializers
    queryset = Location.objects.all()
    permission_classes = [AllowAny]  # Or [AllowAny] for testing
