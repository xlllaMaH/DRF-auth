from rest_framework import viewsets, status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.generics import RetrieveAPIView, 

from rest_framework_simplejwt.tokens import RefreshToken

from users.models import CustomUserModel
from .serializers import UserSerializer, LoginSerializer, RegisterSerializer


class LoginView(APIView):
    """Класс логина(сделать post(?))"""

    # Добавить пермишены + вариант авторизации
    def post(self, request):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user'] #Захватить то что сделали в сериализаторе
            refresh = RefreshToken.for_user(user)

            return Response({
                'token': {
                    'access': str(refresh.access_token),
                    'refresh': str(refresh)
                },
                'user': {
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name

                }
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class UserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny] # По идее надо сделать чтобы все могли
