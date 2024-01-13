from django.urls import path
from .views import  DepositMoneyView


urlpatterns = [
    path("deposit/", DepositMoneyView.as_view(), name="deposit"),
]