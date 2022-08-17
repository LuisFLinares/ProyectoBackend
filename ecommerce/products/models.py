from django.db import models


class Categories(models.Model):
    categoryId = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=200)
    categoryDescription = models.CharField(max_length=200)
    condition = models.BooleanField(default=True, null=True)

    class Meta:
        db_table = 'categories'    

class Products(models.Model):
    productId = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=200, null=False)
    productDescription = models.CharField(max_length=200)
    productPrice = models.DecimalField(max_digits=5, decimal_places=2)
    condition = models.BooleanField(default=True, null=True)
    categorieId = models.ForeignKey(Categories, on_delete=models.CASCADE, default= 1, related_name='ProductsCategory')

    class Meta:
        db_table = 'products'

