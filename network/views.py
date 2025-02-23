from rest_framework import viewsets, permissions
from .models import NetworkNode
from .serializers import NetworkNodeSerializer, NetworkNodeCreateSerializer


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return NetworkNodeCreateSerializer
        return NetworkNodeSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        country = self.request.query_params.get('country', None)
        if country:
            return NetworkNode.objects.filter(contacts__country=country)
        return NetworkNode.objects.all()
