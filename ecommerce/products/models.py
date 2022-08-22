from django.db import models
from datetime import datetime
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Categories(models.Model):
    categoryId = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=200)
    categoryDescription = models.CharField(max_length=200)
    categoryStatus = models.BooleanField(default=True, null=True)

    class Meta:
        db_table = 'categories'    

class Products(models.Model):
    productId = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=200, null=False)
    productDescription = models.CharField(max_length=200)
    productPrice = models.DecimalField(max_digits=5, decimal_places=2)
    productImage = models.TextField(default='https://www.google.com')
    productStatus = models.BooleanField(default=True, null=True)
    categorieId = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

class Purchase(models.Model):
    purchaseId = models.AutoField(primary_key=True)
    purchaseCreated = models.DateTimeField(default=datetime.now())
    purchaseStatus = models.BooleanField(default=True)
    purchaseTotal = models.DecimalField(max_digits=5, decimal_places=2)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table= 'purchase'

class PurchaseDetail(models.Model):
    purchaseDetailId = models.AutoField(primary_key=True)
    purchaseDetailAmount = models.DecimalField(max_digits=5, decimal_places=2)
    productId = models.ForeignKey(Products, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'purchase_detail'

