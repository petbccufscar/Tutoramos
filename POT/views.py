from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from POT.models import POT
from POT.serializers import POTSerializer
# Create your views here.

class ListCreatePOT(generics.ListCreateAPIView):
    queryset = POT.objects.all()
    serializer_class = POTSerializer
    permission_classes = [IsAuthenticated]

class RetrieveUpdateDeletePOT(generics.RetrieveUpdateDestroyAPIView):
    queryset = POT.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = POTSerializer