from django.shortcuts import render
from .models import POT
from rest_framework.generics import ListCreateAPIView
from .serializers import POTSerializer

# Create your views here.
# List Create
class LCPOT(ListCreateAPIView):
    queryset = POT.objects.all()
    serializer_class = POTSerializer
    permission_classes = []