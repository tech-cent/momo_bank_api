from django.urls import path
from account.views import AccountView, AccountDetail


app_name = "account"
urlpatterns = [
    path('', AccountView.as_view(), name="base"),
    path('<int:pk>/', AccountDetail.as_view(), name="detail"),
]
