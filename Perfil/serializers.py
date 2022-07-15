from rest_framework import serializers

from POT.models import POT
from .models import Perfil
from django.contrib.auth.models import User
from django.db import transaction

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'name']

    password = serializers.CharField(
        write_only=True,
        min_length=2,
        max_length=200,
    )
    name = serializers.CharField(
        min_length=2,
        max_length=200,
    )

    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(required=True)

    def create(self, validated_data):
        user = User()

        user.username = validated_data['username']
        user.email = validated_data['email']
        user.first_name = validated_data['name']
        validated_data.pop('name')
        user.set_password(validated_data['password'])

        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
            validated_data.pop('password')
        instance.first_name = validated_data['name']
        validated_data.pop('name')

        return super().update(instance, validated_data)


class UnifiedProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = [
            'user',
            'cor_favorita',
            'POT'
        ]
        
    user: User = UserSerializer(write_only=True)
    POT = serializers.PrimaryKeyRelatedField(queryset=POT.objects.all())
    
    @transaction.atomic
    def create(self, validated_data):
        user_data = validated_data.pop('user')

        user = User.objects.create_user(
            first_name=user_data['name'],
            username=user_data['username'],
            email=user_data['email'],
            password=user_data['password']
        )

        return Perfil.objects.create(**validated_data, user=user)

    @transaction.atomic
    def update(self, validated_data):
        user_data = validated_data.pop('user')

        user = User.objects.update(
            name=user_data['name'],
            username=user_data['username'],
            email=user_data['email'],
            password=user_data['password']
        )

        return Perfil.objects.update(**validated_data, user=user)

    def to_representation(self, instance):
        representation = {'id': instance.user.id,
                          'username': instance.user.username,
                          'email': instance.user.email,
                          'nome': instance.user.get_full_name()
                          }

        # Adiciona os dados da própria instância.
        representation.update(super().to_representation(instance))
        return representation