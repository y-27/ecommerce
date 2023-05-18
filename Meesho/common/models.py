from django.db import models

# Create your models here.

class Seller(models.Model) :
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 200 ,default='')
    e_mail = models.CharField(max_length = 30)
    gender = models.CharField(max_length = 30 ,default='')
    phone_no = models.BigIntegerField(default=1) 
    photo = models.ImageField(upload_to  = 'seller/',default='' )
    company_name = models.CharField(max_length = 30 ,default='')
    user_name= models.IntegerField(default= 1 )
    password = models.CharField(max_length = 20 ,default = '')
    ac_holder_name = models.CharField(max_length = 30 ,default = '')
    ifsc = models.CharField(max_length = 20, default = '')
    branch= models.CharField(max_length = 30, default = '')
    ac_no = models.CharField(max_length = 30, default = '')

    class Meta:
        db_table = 'seller_tb'



