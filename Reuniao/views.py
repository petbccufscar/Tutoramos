from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from Reuniao.models import Reuniao
from Reuniao.serializers import ReuniaoSerializer

# Create your views here.
class ListCreateReuniao(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReuniaoSerializer

    def get_queryset(self):
        qs = Reuniao.objects.all()
        return qs.filter(POT=self.request.user.perfil.POT)

class RetrieveUpdateDeleteReuniao(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reuniao.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ReuniaoSerializer