from decimal import Decimal
from rest_framework.test import APITestCase
from .models import Wallet


class WalletAPITest(APITestCase):
    def setUp(self):
        self.wallet = Wallet.objects.create()

    def test_deposit(self):
        resp = self.client.post(
            f"/api/v1/wallets/{self.wallet.id}/operation/",
            {"operation_type": "DEPOSIT", "amount": "100.00"},
            format="json",
        )
        self.assertEqual(resp.status_code, 200)
        self.wallet.refresh_from_db()
        self.assertEqual(self.wallet.balance, Decimal("100.00"))

    # wallets/tests.py
    from decimal import Decimal
    from rest_framework.test import APITestCase
    from .models import Wallet

    class WalletAPITest(APITestCase):
        def setUp(self):
            self.wallet = Wallet.objects.create()

        def test_deposit(self):
            resp = self.client.post(
                f"/api/v1/wallets/{str(self.wallet.id)}/operation/",
                {"operation_type": "DEPOSIT", "amount": "100.00"},
                format="json",
            )
            self.assertEqual(resp.status_code, 200)
            self.wallet.refresh_from_db()
            self.assertEqual(self.wallet.balance, Decimal("100.00"))

        def test_withdraw_success(self):
            self.wallet.balance = Decimal("200.00")
            self.wallet.save()

            resp = self.client.post(
                f"/api/v1/wallets/{str(self.wallet.id)}/operation/",
                {"operation_type": "WITHDRAW", "amount": "50.00"},
                format="json",
            )
            self.assertEqual(resp.status_code, 200)
            self.wallet.refresh_from_db()
            self.assertEqual(self.wallet.balance, Decimal("150.00"))

        def test_withdraw_insufficient_funds(self):
            # баланс 0, пытаемся снять 50
            resp = self.client.post(
                f"/api/v1/wallets/{str(self.wallet.id)}/operation/",
                {"operation_type": "WITHDRAW", "amount": "50.00"},
                format="json",
            )
            self.assertEqual(resp.status_code, 400)
            self.wallet.refresh_from_db()
            self.assertEqual(self.wallet.balance, Decimal("0.00"))

        def test_get_balance(self):
            # заранее кладем деньги
            self.wallet.balance = Decimal("300.00")
            self.wallet.save()

            resp = self.client.get(f"/api/v1/wallets/{str(self.wallet.id)}/")
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(
                resp.json(), {"wallet_id": str(self.wallet.id), "balance": "300.00"}
            )
