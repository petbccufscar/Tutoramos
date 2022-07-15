from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from .models import Perfil
from .serializers import UnifiedProfileSerializer
# Create your views here.

# List Create
class LCPerfil(ListCreateAPIView):
    queryset = Perfil.objects.all()
    serializer_class = UnifiedProfileSerializer
    permission_classes = []