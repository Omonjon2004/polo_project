from rest_framework import serializers
from rest_framework.fields import CharField

from apps.account.models import Users


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'avatar', 'gender']

