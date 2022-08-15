from itertools import product
from django.shortcuts import render
from rest_framework import generics,  status
from rest_framework.response import Response
from .models import Products
from .serializers import ProductSerializer

class ProductView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def get(self, request):
       products = self.get_serializer(self.get_queryset(), many=True)

       return Response(data={
       'success': True,
       'message':'la lista de productos es',
       'content': products.data
       }, status=status.HTTP_200_OK)

    def post(self, request):
       product = self.get_serializer(data=request.data)
       if product.is_valid():
          product.save()
          return Response(data={
            'success':True,
            'message': '',
            'content': product.data
          }, status=status.HTTP_201_CREATED)
