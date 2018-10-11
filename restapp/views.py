from analysis.models import StockList, WatchList, MarketLogD, MarketLogDs
from restapp.serializers import StockListSerializer, WatchListSerializer, MarketLogDSerializer,  MarketLogDsSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

class StockListViewSet(viewsets.ModelViewSet):
    queryset=StockList.objects.all()
    serializer_class=StockListSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = '__all__'
    ordering_fields = '__all__'

class WatchListViewSet(viewsets.ModelViewSet):
    queryset=WatchList.objects.all()
    serializer_class=WatchListSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = '__all__'
    ordering_fields = '__all__'

class MarketLogDViewSet(viewsets.ModelViewSet):
    queryset=MarketLogD.objects.all()
    serializer_class=MarketLogDSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = '__all__'
    ordering_fields = '__all__'
    
class MarketLogDsViewSet(viewsets.ModelViewSet):
    queryset=MarketLogDs.objects.all()
    serializer_class=MarketLogDsSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = '__all__'
    ordering_fields = '__all__'


# Create your views here.
