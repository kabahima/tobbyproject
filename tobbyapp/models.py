
from concurrent.futures.process import _MAX_WINDOWS_WORKERS
# from ssl import Options
from django.db import models


# Create your models here.
class electrical(models.Model):
    itemname=models.CharField(max_length=20)
    itemprice=models.CharField(max_length=20)
    itemquantity=models.CharField(max_length=20)
    totalamount=models.CharField(max_length=20)
    image=models.ImageField(upload_to=None,height_field=None,width_field=None,max_length=200)

    def __str__(self):
           
        return self.Name

class salon(models.Model):
    itemname=models.CharField(max_length=20)
    itemprice=models.CharField(max_length=20)
    itemquantity=models.CharField(max_length=100)
    totalamount=models.CharField(max_length=20)
    image=models.ImageField(upload_to=None,height_field=None,width_field=None,max_length=200)

    def __str__(self):
           
        return self.Name

class welding(models.Model):
    itemname=models.CharField(max_length=20)
    itemprice=models.CharField(max_length=20)
    itemquantity=models.CharField(max_length=100)
    totalamount=models.CharField(max_length=20)
    image=models.ImageField(upload_to=None,height_field=None,width_field=None,max_length=200)

    def __str__(self):
       
        return self.Name