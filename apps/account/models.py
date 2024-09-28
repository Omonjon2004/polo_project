from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.product.choices import Gender_List
from apps.shared.models import TimeStampedModel


# Create your models here.


class Users(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True)
    avatar = models.ImageField(upload_to='avatars/')
    gender = models.CharField(choices=Gender_List, max_length=20)
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.get_full_name()



class UsersCards(TimeStampedModel):
    card_number = models.CharField(max_length=255, unique=True)
    expiration_date = models.DateField()
    card_token = models.CharField(max_length=255)
    cvv = models.IntegerField()
    account = models.ForeignKey(to=Users, on_delete=models.SET_NULL, null=True)