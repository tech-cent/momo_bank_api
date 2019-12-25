from django.db import IntegrityError
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from account.serializers import AccountSerializer


class AccountView(APIView):
    """
    Crud operations on the Account model
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Create a bank account for the user logged in.
        """
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """
        Return all accounts belonging to the user logged in.
        """
        accounts = request.user.account_set.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)
