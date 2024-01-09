from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from fornecedor.views import FornecedorViewSet
from cliente.views import ClienteViewSet
from estado.views import EstadoViewSet
from login.views import CreateUserViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clientes', ClienteViewSet, basename='Clientes')
router.register('fornecedores', FornecedorViewSet, basename='Fornecedores')
router.register('estados', EstadoViewSet, basename='Estados')
router.register('status', EstadoViewSet, basename='Status')
router.register('cadastro', CreateUserViewSet, basename='cadastro')

urlpatterns = [
    path("admin/", admin.site.urls),
    # OpenApi 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # Autenticação
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/cadastro/<int:pk>/', CreateUserViewSet.as_view({'put': 'update'}), name='user-detail'),
    path("api/", include(router.urls)),
]
