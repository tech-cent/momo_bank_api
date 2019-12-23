from django.urls import path
from bank.views import BankView

app_name = "bank"
urlpatterns = [
    path('', BankView.as_view(), name="base"),
]
