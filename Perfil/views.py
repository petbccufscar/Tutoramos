from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from Perfil.models import Perfil
from Perfil.serializers import PerfilSerializer

# Create your views here.
class ListCreatePerfil(generics.ListCreateAPIView):
    queryset = Perfil.objects.all()
    permission_classes = []
    serializer_class = PerfilSerializer

class RetrieveUpdatePerfil(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PerfilSerializer

    def get_queryset(self):
        qs = Perfil.objects.all()
        if self.request.method == 'GET':
            return qs
        return qs.filter(id=self.request.user.perfil.id)