from django.shortcuts import render
from analysis.models import MarketLogD, WatchList,StockList
from twstock import Stock 
# Create your views here.

def index(request):
    V_MarketLogD=MarketLogD.objects.all()
    V_StockName=StockList.objects.all()
  
    return render(request, 'MarketWatch/index.html',locals())

def personallist(request):
    V_MarketLogD=MarketLogD.objects.all()
    V_StockName=StockList.objects.all()
    V_WatchListIdx=WatchList.objects.all()
    return render(request, 'MarketWatch/personallist.html',locals())

#   def T(request):
#     V_MarketLogD=MarketLogD.objects.all()
#     V_StockName=StockList.objects.all()
#     # accountId = 1
#     # watchlist = WatchList.objects.filter(accountId=accountId)
#     # print(watchlist)
#     # for stock in V_MarketLogD, Stocklist:
#     #     print(item.stocktag)
#     #     stock = Stock(item.stocktag)
#     #     print(stock.data[-1])
#     #     print(stock.data[-1][0])
#     #     print(stock.data[-1][1])
#     #     print(stock.data[-1][2])
#     #     print(stock.data[-1][3])

#     # print(stocks)
#     return render(request, 'MarketWatch/index.html',locals())  