from itertools import product
from django.shortcuts import render
from rest_framework import generics,  status
from rest_framework.response import Response
from .models import Categories, Products
from .serializers import CategoriesSerializer, ProductsSerializer

class ProductsView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

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

class CategoriesView(generics.ListCreateAPIView):
   queryset = Categories.objects.filter(condition=True).all()
   serializer_class = CategoriesSerializer

   def get(self,request):
      categories = self.get_serializer(self.get_queryset(), many=True)

      return Response(data={
         'success': True,
         'message': 'a lista de productos es',
         'content': categories.data
      }, status=status.HTTP_200_OK)

   def post(self, request):
      category = self.get_serializer(data=request.data)
      if category.is_valid():
         category.save()
         return Response(data={
            'success': True,
            'message': '',
            'content': category.data
         }, status=status.HTTP_201_CREATED) 
