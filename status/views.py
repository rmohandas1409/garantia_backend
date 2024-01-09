from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from status.models import Status
from status.serializer import StatusSerializer

class EstadoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os status"""
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    authentication_classes = [JWTAuthentication]
    #permission_classes = [IsAuthenticated, DjangoModelPermissions]
    permission_classes = [AllowAny]
