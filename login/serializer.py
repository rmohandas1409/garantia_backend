from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

#Ao criar o serializer, devemos sobre-escrever o método create. Isso é necessário para não gravar a senha em texto
# claro no banco de dados(com o auxílio da função make_password, primeira ocorrência), essa função vai gerar um hash
# do atributo password que é enviado na requisição. Após fazer o hash do atributo senha, é que salvamos o nosso
# modelo no banco de dados.
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id','username', 'email', 'password', 'first_name', 'last_name', 'is_active', 'is_superuser']

    def create(self, validated_data):

        is_active = validated_data.pop('is_active', False)

        validated_data['password'] = make_password(validated_data.get('password'))
        user = super(UserSerializer, self).create(validated_data)

        user.is_active = is_active
        user.save()

        return user

    def put(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.is_active = validated_data.get('is_active', instance.is_active)

        # Atualizar a senha apenas se for fornecida na requisição
        password = validated_data.get('password')
        if password:
            instance.password = make_password(password)

        instance.save()
        return instance


