from rest_framework import serializers
from account.models import Account


class AccountSerializer(serializers.ModelSerializer):
    """
    Serializer for account modal.
    """
    class Meta:
        model = Account
        fields = [
            'id',
            'type',
            'balance',
            'date_modified',
            'date_created',
            'user',
            'bank'
            ]
        read_only_fields = [
            'id', 'date_modified', 'date_created', 'balance', 'user']

    def create(self, validated_data):
        account = Account()
        account.type = validated_data.get('type')
        account.balance = 0
        account.user = validated_data.get('user')
        account.bank = validated_data.get('bank')
        account.save()
        return account
