from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restapp import views

router=DefaultRouter()
router.register(r'StockList',views.StockListViewSet)
router.register(r'WatchList',views.WatchListViewSet)
router.register(r'MarketLogD',views.StockListViewSet)
router.register(r'MarketLogDs',views.WatchListViewSet)

urlpatterns=[
    path('',include(router.urls))
]