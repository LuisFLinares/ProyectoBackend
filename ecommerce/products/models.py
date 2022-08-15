from django.db import models

#Create your models here.
class Products(models.Model):
    productId = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=200, null=False)
    condition = models.BooleanField(default=True, null=True)
    productDescription = models.CharField(max_length=200)
    productPrice = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'products'
