from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, EmailField
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.account.models import Users


class LoginSerializer(TokenObtainPairSerializer):
    email = EmailField()
    password = CharField()

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        try:
            user = Users.objects.get(email=email)
        except Users.DoesNotExist:
            raise ValidationError(detail="User with this email not found.", code="email")

        user = authenticate(email=email, password=password)
        if user is None:
            raise ValidationError(detail="Incorrect password.", code="password")

        if not user.is_active:
            raise ValidationError(detail="User account is not active.", code="account_inactive")

        return super().validate(attrs)




    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token