from django.shortcuts import render
from rest_framework import generics

from Perfil.models import Perfil
from Perfil.serializers import PerfilSerializer

# Create your views here.
class ListCreatePerfil(generics.ListCreateAPIView):
    queryset = Perfil.objects.all()
    permission_classes = []
    serializer_class = PerfilSerializer

class RetrieveUpdatePerfil(generics.RetrieveUpdateAPIView):
    queryset = Perfil.objects.all()
    permission_classes = []
    serializer_class = PerfilSerializer

