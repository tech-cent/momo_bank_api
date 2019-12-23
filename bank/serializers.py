from rest_framework import serializers
from bank.models import Bank


class BankSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    tin = serializers.CharField(required=True, max_length=100)
    district = serializers.CharField(required=True, max_length=100)
    country = serializers.CharField(required=True, max_length=50)

    def create(self, validated_data):
        bank = Bank()
        bank.name = validated_data.get('name')
        bank.tin = validated_data.get('tin')
        bank.district = validated_data.get('district')
        bank.country = validated_data.get('country')
        bank.save()
        return bank
