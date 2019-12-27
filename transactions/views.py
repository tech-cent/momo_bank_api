from django.shortcuts import render
from django.db import IntegrityError
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from transactions.serializers import TransactionSerializer
from transactions.models import Transaction


class TransactionView(APIView):
    """
    Return a list of transactions,
    Create a new transaction.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Create a new transaction
        """
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """
        Return all transactions in the system.
        """
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)
