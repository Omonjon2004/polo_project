from django.db import models
from django.forms import FloatField

from apps.product.choices import Bags_Category_List, Shoes_Brand_List, \
    Shoes_size_List, Shoes_Category_List, Dress_size_List, Dress_Brand_List, Dress_Category_List, Jewelry_Brand_List, \
    Jewelry_Category_List, Jackets_Brand_List, Jackets_Category_list, Electrical_Brand_List, Electrical_Category_list
from apps.shared.models import BaseProduct


# Create your models here.

class Bags(BaseProduct):
    brand = models.CharField(max_length=100,blank=True,null=True)
    ##brendi yuq bo'lishi ham mumkin blank true shunga
    image = models.ImageField(upload_to='bags_images/')
    category=models.CharField(max_length=100,choices=Bags_Category_List)

class Shoes(BaseProduct):
    brand=models.CharField(max_length=100,choices=Shoes_Brand_List,blank=True ,null=True)
    ##brendi yuq bo'lishi ham mumkin blank true shunga
    size=models.IntegerField(max_length=2,choices=Shoes_size_List)
    image = models.ImageField(upload_to='shoes_images/')
    category=models.CharField(max_length=100,choices=Shoes_Category_List)


class Dress(BaseProduct):
    brand = models.CharField(max_length=100, choices=Dress_Brand_List,blank=True ,null=True)
    ##brendi yuq bo'lishi ham mumkin blank true shunga
    size = models.CharField(max_length=5,choices=Dress_size_List)
    image = models.ImageField(upload_to='dress_images/')
    category=models.CharField(max_length=100,choices=Dress_Category_List)

class Jewelry(BaseProduct):
    brand=models.CharField(max_length=50,choices=Jewelry_Brand_List,blank=True ,null=True)
    ##brendi yuq bo'lishi ham mumkin blank true shunga
    weight=FloatField(max_digits=5,decimal_places=2)
    image = models.ImageField(upload_to='jewelry_images/')
    size=models.DecimalField(max_digits=5,decimal_places=2)
    category=models.CharField(max_length=255,choices=Jewelry_Category_List)
    composition=models.DecimalField(max_digits=5,decimal_places=2 ,default=None)# probasi uchun uzuklarni

class Jackets(BaseProduct):
    brand=models.CharField(max_length=50,choices=Jackets_Brand_List,blank=True ,null=True)
    ##brendi yuq bo'lishi ham mumkin blank true shunga
    image = models.ImageField(upload_to='jackets_images/')
    category=models.CharField(max_length=255,choices=Jackets_Category_list)
    size = models.CharField(max_length=5,choices=Dress_size_List)

class Electrical(BaseProduct):
    brand=models.CharField(max_length=50,choices=Electrical_Brand_List)
    image = models.ImageField(upload_to='electrical_images/')
    category=models.CharField(max_length=255,choices=Electrical_Category_list)
















