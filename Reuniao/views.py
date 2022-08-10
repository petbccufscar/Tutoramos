from rest_framework import generics

from Reuniao.models import Reuniao
from Reuniao.serializers import ReuniaoSerializer

# Create your views here.
class ListCreateReuniao(generics.ListCreateAPIView):
    queryset = Reuniao.objects.all()
    permission_classes = []
    serializer_class = ReuniaoSerializer

class RetrieveUpdateDeleteReuniao(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reuniao.objects.all()
    permission_classes = []
    serializer_class = ReuniaoSerializer