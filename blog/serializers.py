from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Blog, Category, Tag


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['category']


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class BlogSerializer(ModelSerializer):
    author = UserSerializer()
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Blog
        fields = '__all__'
