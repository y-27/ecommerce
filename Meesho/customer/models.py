from django.db import models

# Create your models here.


class Customer(models.Model) :
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 200)
    e_mail = models.CharField(max_length = 30)
    gender = models.CharField(max_length = 30)
    phone = models.BigIntegerField() 
    password = models.CharField(max_length = 20)


    class Meta:
        db_table = 'customer_tb'