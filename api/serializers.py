from rest_framework import serializers
from post.models import Post 

class PostListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ['title', 'author', 'slug', 'content', 'publish']

class PostDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ['id','title', 'author', 'slug', 'content', 'publish', 'draft']

class PostCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ['title', 'content', 'publish', 'draft']
