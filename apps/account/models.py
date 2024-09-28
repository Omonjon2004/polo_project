from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from apps.product.choices import Gender_List
from apps.shared.models import TimeStampedModel


class Users(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True, default=None)
    gender = models.CharField(choices=Gender_List, max_length=20)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    def __str__(self):
        return self.get_full_name()


class UsersCards(TimeStampedModel):
    card_name  = models.CharField(max_length=50)
    card_number =models.CharField(
        max_length=16,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d{16}$',
                message='Card number must be exactly 16 digits.'
            )
        ]
    )
    expiration_date = models.CharField(
        max_length=5,
        validators=[
            RegexValidator(
                regex=r'^(0[1-9]|1[0-2])\/\d{2}$',
                message='Expiration date must be in MM/YY format.'
            )
        ]
    )
    cvv = models.CharField(
        max_length=3,
        validators=[
            RegexValidator(
                regex=r'^\d{3}$',
                message='CVV must be exactly 3 digits.'
            )
        ]
    )
    account = models.ForeignKey(to=Users,on_delete=models.CASCADE,related_name='cards')
