from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Wallet, WalletOperation
from .serializers import OperationSerializer
from django.shortcuts import get_object_or_404
from django.db import transaction


class WalletOperationView(APIView):
    def post(self, request, wallet_id):
        serializer = OperationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        op_type = serializer.validated_data["operation_type"]
        amount = serializer.validated_data["amount"]  # Decimal

        with transaction.atomic():
            wallet = get_object_or_404(Wallet.objects.select_for_update(), id=wallet_id)
            prev = wallet.balance

            if op_type == "DEPOSIT":
                wallet.balance = prev + amount
            elif op_type == "WITHDRAW":
                if prev < amount:
                    return Response(
                        {"error": "Не хватает средств"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                wallet.balance = prev - amount

            wallet.save()
            WalletOperation.objects.create(
                wallet=wallet,
                operation_type=op_type,
                amount=amount,
                previous_balance=prev,
                resulting_balance=wallet.balance,
            )

        return Response(
            {"wallet_id": str(wallet.id), "balance": str(wallet.balance)},
            status=status.HTTP_200_OK,
        )


class WalletDetailView(APIView):
    def get(self, request, wallet_id):
        wallet = get_object_or_404(Wallet, id=wallet_id)
        return Response({"wallet_id": str(wallet.id), "balance": str(wallet.balance)})
