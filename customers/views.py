from django.shortcuts import render
from .models import Customer, Blog, Comment
from .serializer import CustomerSerializer, BlogSerializer, CommentSerializer
from rest_framework import mixins , generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .paginations import CustomerPagination
from .filters import CustomerFilter
from rest_framework.filters import SearchFilter,OrderingFilter


# Mixins Class base Views
'''
class Customers(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    

class CustomersDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self, request, pk):
        return self.update(request,pk)
    
    def delete(self, request,pk):
        return self.destroy(request,pk)
    
'''    

'''
# Generics base Class View

#class Customers(generics.ListAPIView,generics.CreateAPIView):

class Customers(generics.ListCreateAPIView):    
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


#class CustomersDetail(generics.UpdateAPIView,generics.RetrieveAPIView,generics.DestroyAPIView):
class CustomersDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'pk'

'''

# Viewset   
'''
class Customers(viewsets.ViewSet):

    def list(self,request):
        queryset = Customer.objects.all()
        serialiazer = CustomerSerializer(queryset,many=True)
        return Response(serialiazer.data)
    
    def create(self,request):
        serializer = CustomerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def retrieve(self,request,pk=None):
        customer = get_object_or_404(Customer,pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
    def update(self,request,pk=None):
        customer = get_object_or_404(Customer,pk=pk)
        serializer = CustomerSerializer(customer,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
        
    def destroy(self,request,pk=None):
        customer = get_object_or_404(Customer,pk=pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
'''    
# viewsets used for ModelViewSet


class Customers(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    #pagination_class = CustomerPagination # Filter is Working After Comment this
    #filterset_fields = ['cname']
    filterset_class = CustomerFilter


class Blogs(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    #search_fields = ['^title'] # first started title search
    search_fields = ['title','desc']
    Ordering_fileds = ['cid']

class Comments(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'    