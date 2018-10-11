from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router=DefaultRouter()
router.register(r'account',views.AccountViewSet)
router.register(r'coin',views.CoinViewSet)
router.register(r'balance',views.BalanceViewSet)
router.register(r'tradehistory',views.TradeHistoryViewSet)

urlpatterns=[
    path('',include(router.urls))
]