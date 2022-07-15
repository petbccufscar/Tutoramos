from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Reuniao
from .serializers import ReuniaoSerializer
# Create your views here.

# List Create
class LCReuniao(ListCreateAPIView):
    queryset = Reuniao.objects.all()
    serializer_class = ReuniaoSerializer
    permission_classes = []