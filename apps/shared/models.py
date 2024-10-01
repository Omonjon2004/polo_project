from django.db import models

from apps.product.choices import Color_List, Gender_List, RATING_List, Season_List, Category_List, Brand_List


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class BaseProduct(TimeStampedModel):
    brand=models.CharField(max_length=100,choices=Brand_List,blank=True,null=True)
    color = models.CharField(max_length=100, choices=Color_List)
    price = models.FloatField()
    gender = models.CharField(max_length=20, choices=Gender_List)
    rating = models.DecimalField(max_digits=2, decimal_places=1, choices=RATING_List, blank=True,null=True)
    by_count = models.IntegerField(default=0)
    sale_count = models.IntegerField(default=0)
    discount = models.FloatField(default=0)
    season = models.CharField(max_length=100, choices=Season_List)
    category = models.CharField(max_length=100, choices=Category_List, blank=True,null=True)



    class Meta:
        abstract = True