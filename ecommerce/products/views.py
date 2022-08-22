from rest_framework import generics,  status
from rest_framework.response import Response
from .models import Categories, Products, Purchase, PurchaseDetail
from .serializers import CategoriesSerializer, ProductsSerializer, PurchaseSerializer, PurchaseDetailSerializer
import cloudinary

class ProductsView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def get(self, request):
       products = self.get_serializer(self.get_queryset(), many=True)

       return Response(data=products.data, status=status.HTTP_200_OK)

    def post(self, request):
       product = self.get_serializer(data=request.data)
       if product.is_valid():
          product.save()
          return Response(data=product.data, status=status.HTTP_201_CREATED)

class CategoriesView(generics.ListCreateAPIView):
   queryset = Categories.objects.filter(categoryStatus=True).all()
   serializer_class = CategoriesSerializer

   def get(self,request):
      categories = self.get_serializer(self.get_queryset(), many=True)

      return Response(data=categories.data,status=status.HTTP_200_OK)

   def post(self, request):
      category = self.get_serializer(data=request.data)
      if category.is_valid():
         category.save()
         return Response(data=category.data, status=status.HTTP_201_CREATED) 

class PurchaseView(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class PurchaseDetailView(generics.ListCreateAPIView):
    queryset = PurchaseDetail.objects.all()
    serializer_class = PurchaseDetailSerializer

class DeleteCategoriesView(generics.DestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class DeleteProductsView(generics.DestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = ProductsSerializer

class DeletePurchaseView(generics.DestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = PurchaseSerializer

class DeletePurchaseDetailView(generics.DestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = PurchaseDetailSerializer

from  rest_framework.permissions import IsAuthenticated

class UploadView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        print(request.user)
        file = request.data.get('picture')

        upload_data = cloudinary.uploader.upload(file)
        return Response(data= upload_data, status=201)
