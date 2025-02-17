"""M2A URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from M2A_app import views

router = DefaultRouter()
router.register(r'empresas', views.EmpresaViewSet)
router.register(r'diagnosticos', views.DiagnosticoViewSet)
router.register(r'usuarios', views.UsuariosViewSet)
router.register(r'questionarios', views.QuestionarioViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_auth_token),
    path('empresafks/', views.EmpresaFKSView.as_view()),
    path('grupos/', views.GruposView.as_view()),
    path('', include(router.urls)),
]
