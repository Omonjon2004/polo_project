from django.db import models
from apps.account.models import Users
from apps.product.models import Bags, Shoes, Dress, Jewelry


class Basket(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, related_name='items', on_delete=models.CASCADE)
    bag = models.ForeignKey(Bags, null=True, blank=True, on_delete=models.CASCADE)
    shoes = models.ForeignKey(Shoes, null=True, blank=True, on_delete=models.CASCADE)
    dress = models.ForeignKey(Dress, null=True, blank=True, on_delete=models.CASCADE)
    jewelry = models.ForeignKey(Jewelry, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_product()} - {self.quantity}"

    def get_product(self):
        if self.bag:
            return self.bag
        elif self.shoes:
            return self.shoes
        elif self.dress:
            return self.dress
        elif self.jewelry:
            return self.jewelry
        return None
from django.db import models

# Create your models here.
