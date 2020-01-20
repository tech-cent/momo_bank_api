from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User
from utils.validate_phonenumber import is_phonenumber_valid


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.CharField(required=False, allow_blank=True)
    password = serializers.CharField(required=True, write_only=True)
    phone_number = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    nin = serializers.CharField(required=True)
    dob = serializers.DateField(required=True)

    def validate(self, attrs):
        """
        Add custom validations
        """
        if not is_phonenumber_valid(attrs['phone_number']):
            raise serializers.ValidationError('Invalid phone number')
        return attrs

    def create(self, validated_data):
        """
        Create and return user instance, given validate data
        """
        user = User()
        user.email = validated_data.get('email')
        user.first_name = validated_data.get('first_name')
        user.last_name = validated_data.get('last_name')
        user.set_password(validated_data.get('password'))
        user.phone_number = validated_data.get('phone_number')
        user.nin = validated_data.get('nin')
        user.dob = validated_data.get('dob')
        user.save()
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Customize token to add user name
    in encoding.
    """
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['name'] = self.user.first_name
        return data
