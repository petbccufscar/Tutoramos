from rest_framework import serializers
from .models import POT

class POTSerializer(serializers.ModelSerializer):
    class Meta:
        model = POT
        fields = '__all__'