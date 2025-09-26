from django.urls import path
from .views import WalletOperationView, WalletDetailView

urlpatterns = [
    path("api/v1/wallets/<uuid:wallet_id>/operation/", WalletOperationView.as_view()),
    path("api/v1/wallets/<uuid:wallet_id>/", WalletDetailView.as_view()),
]

