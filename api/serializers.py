from rest_framework import serializers
from users.models import CustomUserModel
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

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


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=64, write_only=True, required=True, validators=[validate_password])
    password_confirm = serializers.CharField(max_length=64, write_only=True, required=True, validators=[validate_password])
    username = serializers.CharField(max_length=25, required=False, allow_blank=True)

    class Meta:
        model = User
        fields =['email', 'first_name', 'last_name', 'username', 'password', 'password_confirm']

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({'password_confirm': "Пароли не совпадают!"})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        return User.objects.create_user(**validated_data)