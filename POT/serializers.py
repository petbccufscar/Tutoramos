from rest_framework import serializers
from .models import POT
from django.db import transaction

class POTSerializer(serializers.ModelSerializer):
    class Meta:
        model = POT
        fields = '__all__'