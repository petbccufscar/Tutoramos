"""tutoramos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from POT.views import ListCreatePOT, RetrieveUpdateDeletePOT
from Perfil.views import ListCreatePerfil, RetrieveUpdatePerfil
from Reuniao.views import ListCreateReuniao, RetrieveUpdateDeleteReuniao

urlpatterns = [
    path('admin/', admin.site.urls),
    path('POT/', ListCreatePOT.as_view()),
    path('POT/<pk>/', RetrieveUpdateDeletePOT.as_view()),
    path('Reuniao/', ListCreateReuniao.as_view()),
    path('Reuniao/<pk>/', RetrieveUpdateDeleteReuniao.as_view()),
    path('Perfil/', ListCreatePerfil.as_view()),
    path('Perfil/<pk>/', RetrieveUpdatePerfil.as_view()),
]
