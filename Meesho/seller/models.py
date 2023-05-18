from django.db import models
from common.models import Seller

# Create your models here.

class Product(models.Model) :
    product_name = models.CharField(max_length = 30)
    seller = models.ForeignKey(Seller,on_delete= models.CASCADE)
    description = models.CharField(max_length = 100)
    stock = models.IntegerField()
    code = models.CharField(max_length = 30)
    price = models.FloatField()
    image = models.ImageField(upload_to  = 'product/' )
    
    class Meta:
        db_table = 'product_tb'
        




