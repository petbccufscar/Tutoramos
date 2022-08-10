from rest_framework import serializers
from .models import Reuniao

class ReuniaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reuniao
        fields = '__all__'