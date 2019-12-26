from django.urls import path
from transactions.views import TransactionView

app_name = "transactions"
urlpatterns = [
    path('', TransactionView.as_view(), name="base")
]
