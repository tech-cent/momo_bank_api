from django.urls import path
from transactions.views import TransactionView, TransactionDetail

app_name = "transactions"
urlpatterns = [
    path('', TransactionView.as_view(), name="base"),
    path('<int:pk>/', TransactionDetail.as_view(), name="detail"),
]
