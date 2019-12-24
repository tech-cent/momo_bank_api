from django.urls import path
from account.views import AccountView


app_name = "account"
urlpatterns = [
    path('', AccountView.as_view(), name="base"),
]
