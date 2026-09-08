from rest_framework import routers
from django.urls import path, include

from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .views import UserView, LoginView


urlpatterns = [
    path('user/', UserView.as_view(), name='user'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('token/verify/', TokenRefreshView.as_view(), name='verify')
]
