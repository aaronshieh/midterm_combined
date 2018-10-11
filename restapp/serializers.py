from rest_framework import serializers
from analysis.models import StockList, WatchList, MarketLogD, MarketLogDs

class StockListSerializer(serializers.ModelSerializer):
    class Meta:
        model=StockList
        fields='__all__'
class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model=WatchList
        fields='__all__'
class MarketLogDSerializer(serializers.ModelSerializer):
    stockname = serializers.ReadOnlyField(source='stocktag.stockname')
    class Meta:
        model=MarketLogD
        fields='__all__'
class MarketLogDsSerializer(serializers.ModelSerializer):
    class Meta:
        model=MarketLogDs
        fields='__all__'
