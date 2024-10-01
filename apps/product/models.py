from django.db import models
from django.forms import FloatField

from apps.product.choices import Bags_Category_List, \
    Dress_size_List, Jewelry_Brand_List, \
    Jewelry_Category_List, Jackets_Brand_List, Jackets_Category_list, Electrical_Brand_List, Electrical_Category_list, \
    Dress_name_List, Jewelry_name_List, Jackets_name_List, Electrical_name_List, Shoes_name_List, \
    Shoes_size_List, Bags_name_List
from apps.shared.models import BaseProduct


# Create your models here.

class Bags(BaseProduct):
    name = models.CharField(max_length=100,choices=Bags_name_List)
    image = models.ImageField(upload_to='bags_images/')
    category = models.CharField(max_length=100, choices=Bags_Category_List)


class Shoes(BaseProduct):
    name = models.CharField(max_length=100, choices=Shoes_name_List)
    size = models.IntegerField(choices=Shoes_size_List)
    image = models.ImageField(upload_to='shoes_images/')


class Dress(BaseProduct):
    name = models.CharField(max_length=100, choices=Dress_name_List)
    size = models.CharField(max_length=5, choices=Dress_size_List)
    image = models.ImageField(upload_to='dress_images/')


class Jewelry(BaseProduct):
    name = models.CharField(max_length=100, choices=Jewelry_name_List)
    weight = FloatField()
    image = models.ImageField(upload_to='jewelry_images/')
    size = models.DecimalField(max_digits=5, decimal_places=2)
    composition = models.DecimalField(max_digits=5, decimal_places=2, default=None)  # probasi uchun uzuklarni

    brand = models.CharField(max_length=100, choices=Jewelry_Brand_List, blank=True, null=True)
    category = models.CharField(max_length=100, choices=Jewelry_Category_List, blank=True, null=True)


class Jackets(BaseProduct):
    name = models.CharField(max_length=100, choices=Jackets_name_List)
    brand = models.CharField(max_length=50, choices=Jackets_Brand_List, blank=True, null=True)
    ##brendi yuq bo'lishi ham mumkin blank true shunga
    image = models.ImageField(upload_to='jackets_images/')
    category = models.CharField(max_length=255, choices=Jackets_Category_list)
    size = models.CharField(max_length=5, choices=Dress_size_List)


class Electrical(BaseProduct):
    name = models.CharField(max_length=100, choices=Electrical_name_List)
    brand = models.CharField(max_length=50, choices=Electrical_Brand_List)
    image = models.ImageField(upload_to='electrical_images/')
    category = models.CharField(max_length=255, choices=Electrical_Category_list)
