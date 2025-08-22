from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny  # Later change to IsAuthenticated
from .models import Asset
from .serializers import AssetSerializer
from django.http import JsonResponse

def index(request):
    return JsonResponse({"message": "Welcome to IAA Asset Management Backend!"})

class AssetViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing asset instances.
    """
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    permission_classes = [AllowAny]  # Replace with IsAuthenticated if needed
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'category', 'location', 'contributedBy']
    ordering_fields = ['name', 'quantity', 'date']
