from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from estado.models import Estado
from estado.serializer import EstadoSerializer

class EstadoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os estados"""
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    authentication_classes = [JWTAuthentication]
    #permission_classes = [IsAuthenticated, DjangoModelPermissions]
    permission_classes = [AllowAny]


