from django.contrib.auth.hashers import make_password
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.contrib.auth.models import User
from login.serializer import UserSerializer


class CreateUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    #permission_classes = [IsAuthenticated, DjangoModelPermissions]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Imprime o que está sendo recebido no corpo da cadastro
        print("Dados recebidos do frontend: cadastro:", request.data)

        # Restante do código de criação do usuário
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        #Obtem o usuario a ser atualizado
        instance = self.get_object()

        # Imprime o que está sendo recebido no corpo da update
        print("Dados recebidos do frontend: update:", request.data)

        #aqui converte a senha enviada pelo front no formato pbkdf2_sha256.hash padrão do django
        password = make_password(request.data.get('password'))

        #aqui acrecenta o novo valor para ser gravado no banco.
        request.data['password'] = password

        # Atualiza o objeto do usuário com os dados recebidos
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Restante do código de atualização do usuário
        return Response(serializer.data)

