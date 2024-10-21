from .models import *
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
         model = Comment
         fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
         model = User
         fields = '__all__'

