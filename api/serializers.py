from rest_framework import serializers
from users.models import CustomUserModel
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUserModel
        fields = ['id', 'username', 'first_name', 'last_name', 'username']

class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            email=email,
            password=password
        )

        if not user:
            raise serializers.ValidationError("Неверно указан логин или пароль")

        if not user.is_active:
            raise serializers.ValidationError("Данный аккаунт неактивен")

        attrs['user'] = user
        return attrs