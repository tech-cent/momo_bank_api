from rest_framework import serializers
from transactions.models import Transaction
from account.models import Account


class TransactionSerializer(serializers.ModelSerializer):
    """
    Serializer class for the transaction model
    """
    class Meta:
        model = Transaction
        fields = [
            'id',
            'type',
            'amount',
            'prev_balance',
            'new_balance',
            'status',
            'date_created',
            'date_modified',
            'created_by',
            'account'
        ]
        read_only_fields = [
            'id', 'prev_balance', 'new_balance', 'created_by'
        ]

    def create(self, validated_data):
        account = validated_data.get('account')
        transaction = Transaction()
        transaction.account = validated_data.get('account')
        transaction.type = validated_data.get('type')
        transaction.amount = validated_data.get('amount')
        transaction.prev_balance = account.balance
        transaction.calculate_new_balance()
        transaction.created_by = validated_data.get('user')
        transaction.save()
        return transaction

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
