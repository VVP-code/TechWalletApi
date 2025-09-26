import uuid
from django.db import models


class Wallet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)


class WalletOperation(models.Model):
    DEPOSIT = "DEPOSIT"
    WITHDRAW = "WITHDRAW"
    OPERATION_CHOICES = [
        (DEPOSIT, "Deposit"),
        (WITHDRAW, "Withdraw"),
    ]

    wallet = models.ForeignKey(
        Wallet, on_delete=models.CASCADE, related_name="operations"
    )
    operation_type = models.CharField(max_length=10, choices=OPERATION_CHOICES)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    previous_balance = models.DecimalField(max_digits=20, decimal_places=2)
    resulting_balance = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.operation_type} {self.amount} -> {self.resulting_balance} ({self.wallet_id})"
