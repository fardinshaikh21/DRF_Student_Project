from rest_framework import serializers
from .models import Customer, Blog, Comment

class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = "__all__"

class BlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Blog
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = "__all__"        
