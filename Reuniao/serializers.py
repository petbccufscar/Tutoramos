from rest_framework import serializers
from .models import Reuniao
from django.db import transaction

class ReuniaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reuniao
        fields = '__all__'