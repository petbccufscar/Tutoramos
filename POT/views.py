from rest_framework import generics

from POT.models import POT
from POT.serializers import POTSerializer
# Create your views here.

class ListCreatePOT(generics.ListCreateAPIView):
    queryset = POT.objects.all()
    serializer_class = POTSerializer
    permission_classes = []

class RetrieveUpdateDeletePOT(generics.RetrieveUpdateDestroyAPIView):
    queryset = POT.objects.all()
    permission_classes = []
    serializer_class = POTSerializer