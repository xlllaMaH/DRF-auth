from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('api/', include('api.urls'), name='api'),
    path('admin/', admin.site.urls, name='admin'),

    #Документация
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(), name='swagger'),
    path('api/redoc/', SpectacularRedocView.as_view(), name='redoc')
]
