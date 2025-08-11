from django.shortcuts import render
from .models import Customer, Blog, Comment
from .serializer import CustomerSerializer,BlogSerializer,CommentSerializer
from rest_framework import mixins 
from rest_framework import generics
from rest_framework.response import Response


# Create your views here.

class Customers(mixins.ListModelMixins,generics.GenericAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer(queryset,many=True)

    def get(self,request):
        return self.list(request)
