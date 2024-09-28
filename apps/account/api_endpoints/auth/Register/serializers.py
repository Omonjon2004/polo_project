import os
from time import time_ns

from django.template.context_processors import media
from config.settings import base
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField

from apps.account.models import Users


class RegisterSerializer(serializers.ModelSerializer):
    password = CharField(write_only=True)
    password2 = CharField(write_only=True)


    class Meta:
        model = Users
        fields = ('id', 'first_name', 'last_name', 'phone_number', 'email', 'avatar', 'gender', 'password', 'password2')

    def validators_phone_number(self, phone_number):
        if Users.objects.filter(phone_number=phone_number).exists():
            raise ValidationError(detail='This phone number is already in use.', code = 'phone_already_exists')
        return phone_number

    def validators_email(self, email):
        if Users.objects.filter(email=email).exists():
            raise ValidationError(detail="This email is already registered", code = 'email')
        return email

    def create(self, validated_data):
        account = Users.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=str(validated_data['phone_number']),
            gender=validated_data['gender'],
            username=f"user{str(time_ns())[-6:]}",
            email=validated_data['email'],

        )
        if account.gender == 'male':
            account.avatar = os.path.join(base.MEDIA_ROOT, 'avatars', 'male.png')
        else:
            account.avatar = os.path.join(base.MEDIA_ROOT, 'avatars', 'female.png')

        account.set_password(validated_data['password'])
        account.save()
        return account

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise ValidationError(detail='Passwords do not match', code='password')
        return attrs
