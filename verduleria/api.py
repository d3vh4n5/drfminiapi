from .models import Verdura
from rest_framework import viewsets, permissions
from .serializers import VerduraSerializer

class VerduraViewset(viewsets.ModelViewSet):
    queryset= Verdura.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = VerduraSerializer