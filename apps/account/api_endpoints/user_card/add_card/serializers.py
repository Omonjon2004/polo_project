from rest_framework import serializers

from apps.account.models import UsersCards


class UserCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersCards
        fields = ['card_name', 'card_number', 'expiration_date', 'cvv']

    def create(self, validated_data):
        validated_data['account'] = self.context['request'].user
        return super().create(validated_data)
