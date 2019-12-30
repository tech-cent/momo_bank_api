from django.urls import path
from account.views import AccountView, AccountDetail, AccountTransactions


app_name = "account"
urlpatterns = [
    path('', AccountView.as_view(), name="base"),
    path('<int:pk>/', AccountDetail.as_view(), name="detail"),
    path(
        '<int:pk>/transactions/',
        AccountTransactions.as_view(),
        name="transactions")
]
