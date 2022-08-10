from csv import unregister_dialect
from rest_framework import serializers

from POT.serializers import POTSerializer
from .models import Perfil
from django.contrib.auth.models import User
from django.db import transaction

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    username = serializers.CharField()
    name = serializers.CharField()

    def create(self, validated_data):
        user = User()

        user.username = validated_data['username']
        user.email = validated_data['email']
        user.first_name = validated_data['first_name']
        validated_data.pop('name')
        user.set_password(validated_data['password'])

        return user

    def update(self, user: User, validated_data):
        l = ['username', 'email', 'first_name']
        for i in l:
            if i in validated_data:
                setattr(user, i, validated_data[i])

        if 'name' in validated_data:
            validated_data.pop('name')

        if 'password' in validated_data:
            user.set_password(validated_data['password'])
        
        return user

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'username']


class PerfilSerializer(serializers.ModelSerializer):

    user: User = UserSerializer(write_only=True)
    
    class Meta:
        model = Perfil
        fields = '__all__'

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
    def update(self, instance, validated_data):
        if 'user' in validated_data:
            user_data = validated_data.pop('user')
            d = {}

            if 'name' in user_data:
                d['first_name'] = user_data['name']

            l = ['email', 'password', 'username']
            for i in l:
                if i in user_data:
                    d[i] = user_data[i]
            
            serializer = UserSerializer()
            user = serializer.update(user = instance.user,validated_data=d)
            user.save()
            instance.user = user
        return super().update(instance,validated_data=validated_data)

    


    def to_representation(self, instance: Perfil):
        representation = {'id': instance.user.id,
                          'username': instance.user.username,
                          'email': instance.user.email,
                          'nome': instance.user.get_full_name()
                          }

        # Adiciona os dados da própria instância.
        representation.update(super().to_representation(instance))
        return representation