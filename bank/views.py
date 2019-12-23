from django.db import IntegrityError
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from bank.models import Bank
from bank.serializers import BankSerializer


class BankView(APIView):
    """
    Handle CRUD for Bank entity
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = BankSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except IntegrityError:
                return Response(
                    "Bank already exists",
                    status=status.HTTP_400_BAD_REQUEST
                )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        banks = Bank.objects.all()
        serializer = BankSerializer(banks, many=True)
        return Response(serializer.data)
