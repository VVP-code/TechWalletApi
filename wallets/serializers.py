from rest_framework import serializers


class OperationSerializer(serializers.Serializer):
    operation_type = serializers.ChoiceField(choices=["DEPOSIT", "WITHDRAW"])
    amount = serializers.DecimalField(max_digits=15, decimal_places=2)


class WalletSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    balance = serializers.DecimalField(max_digits=20, decimal_places=2)
