from rest_framework import serializers
from django.contrib.auth import get_user_model

from movies.models import Actor

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'password',)


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ['actor_id', 'name']

class ActorSerializer2(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('actor_id', 'name', 'profile_path')
