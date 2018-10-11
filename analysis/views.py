from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.db import connection
from django.db import models
from .models import StockList,Tw50,DebtsRatio9,QuickRatio9,GPMargin9,OPMargin9,NPMargin9,ROE9,RevenueGrowthQoQ9,RevenueGrowthYoY9,EPSfromOP9,EPSafterTax9,EPSYTD9,PBRatio9,QuarterEndStockPrice9,BVperShare9,MarketLogD,MarketLogDs,WatchList
from django.core.files.storage import FileSystemStorage
import os, twstock
import pymongo
import random

# Create your views here.
stock=StockList()
tw50=Tw50()
dbr9=DebtsRatio9()
# qkr9=QuickRatio9()
gpm9=GPMargin9()
# opm9=OPMargin9()
npm9=NPMargin9()
roe9=ROE9()
# rgq9=RevenueGrowthQoQ9()
rgy9=RevenueGrowthYoY9()
# epsfop9=EPSfromOP9()
epsatx9=EPSafterTax9()
# epsytd9=EPSYTD9()
# pbr9=PBRatio9()
qesp9=QuarterEndStockPrice9()
bvps9=BVperShare9()
mld=MarketLogD()
mlds=MarketLogDs()
mongoclient=pymongo.MongoClient()
wl=WatchList()

log=[]
def index(request):
    return render(request,'analysis/index.html')

def editwatchlist(request):
    mld=MarketLogD.objects.all()
    wl=WatchList.objects.filter(accountId=0)
    print("first editing on git....")
    return render(request,'analysis/editwatchlist.html',locals())

def companyinfo(request):
    return render(request,'analysis/companyinfo.html')

def marketwatch(request):
    return render(request,'analysis/marketwatch.html')

def dataupdate(request):
    # HttpResponse(len(lines))
    return render(request,'analysis/dataupdate.html',locals())
#==================================================================    
def fillinstocklist(request):
    stock=StockList.objects.filter()
    stock.delete()
    # try: #================讀入所有股票基本資料==========
    with open('analysis/companyinfo.csv','rt') as file:      
        lines=file.readlines()
        for line in lines:
            fields=line.split(',')
            log.append(fields[1])
            stock.create(stocktag=fields.pop(0),
                stockname=fields.pop(0),
                industry=fields.pop(0),
                segment=fields.pop(0),
                capital=fields.pop(0),
                tw50=not bool(fields.pop(0)),
                mid100=not bool(fields.pop(0)),
                selected=not bool(fields.pop(0)),
                watchlist1=False,
                watchlist2=False,
                watchlist3=False
                )
    # except:
        log.append(line)
    return HttpResponse(log)
    # return render(request,'analysis/dataupdate.html',locals())

def marktw50(request):
    str=" 光寶科（臺證所：2301） · 聯電（臺證所：2303） · 臺達電（臺證所：2308） · 鴻海（臺證所：2317） · 國巨（臺證所：2327） · 臺積電（臺證所：2330） · 鴻準（臺證所：2354） · 華碩（臺證所：2357） · 廣達（臺證所：2382） · 研華（臺證所：2395） · 南亞科（臺證所：2408） · 友達（臺證所：2409） · 中華電（臺證所：2412） · 聯發科（臺證所：2454） · 可成（臺證所：2474） · 華新科（臺證所：2492） · 大立光（臺證所：3008） · 臺灣大（臺證所：3045） · 日月光（臺證所：3711） · 群創（臺證所：3481） · 遠傳（臺證所：4904） · 和碩（臺證所：4938） · 臺泥（臺證所：1101） · 亞泥（臺證所：1102） · 統一（臺證所：1216） · 臺塑（臺證所：1301） · 南亞（臺證所：1303） · 臺化（臺證所：1326） · 遠東新（臺證所：1402） · 中鋼（臺證所：2002） · 正新（臺證所：2105） · 臺灣高鐵（臺證所：2633） · 統一超（臺證所：2912） · 臺塑化（臺證所：6505） · 寶成（臺證所：9904） · 彰銀（臺證所：2801） · 中壽（臺證所：2823） · 華南金（臺證所：2880） · 富邦金（臺證所：2881） · 國泰金（臺證所：2882） · 開發金（臺證所：2883） · 玉山金（臺證所：2884） · 元大金（臺證所：2885） · 兆豐金（臺證所：2886） · 臺新金（臺證所：2887） · 永豐金（臺證所：2890） · 中信金（臺證所：2891） · 第一金（臺證所：2892） · 中租KY（臺證所：5871） · 合庫金（臺證所：5880）"
    str=str.replace("（臺證所："," ")
    str=str.replace("） · "," ")
    str=str.replace("）"," ")
    # print(str)
    str=str.strip()
    list=str.split(" ")
    for i in range(len(list)):
        if i%2==1:
            Tw50.objects.create(stocktag=list[i],stockname=list[i-1])
        else:
            continue
    sep=','
    str=sep.join(list)+sep
    # with open('analysis/csv-tw50','w+') as file:    
    #     log=file.write(str)
    tw50=Tw50.objects.filter()
    stocks=StockList.objects.filter(stocktag__in=tw50)
    for stock in stocks:
        stock.tw50=True
        stock.save()
    return HttpResponse(log)

def markmid100(reques):
    with open('analysis/mid100.csv','rt') as file:
        lines=file.readlines()
        fields=[]
        for line in lines:
            line=line.replace('?','')
            line=line.replace('\n','')
            fields=line.split(',')
            print(fields)
            try:
                stock=StockList.objects.get(stocktag=fields.pop(0))
                stock.mid100=True
                print(stock.mid100)
                stock.save()               
            except:
                pass
            log=stock
    return HttpResponse(log)

def select(request):
    log=marktw50(request)
    log=markmid100(request)
    stocks=StockList.objects.all()
    for stock in stocks:
        stock.selected=stock.tw50 or stock.mid100
        stock.save()
    log=stock.stockname
    return HttpResponse(log)
# #=====================================================================
def create9(request,filename,Obj):
    # print(filestr)
    # print(obj)
    log=[]
    if Obj:
        obj=Obj.objects.filter()
        obj.delete()
        if filename=='clear':
            log.append('檔案已清空')
            return log
    #-------以上先把檔案清空------------
        with open(filename,'rt') as file:      
            lines=file.readlines()
            for line in lines:
                fields=line.split(',')
                try:
                    stock=StockList.objects.get(stocktag=fields.pop(0))
                    #------只更新selected list 減少資料檔數--------------
                    if stock.selected:
                        obj.create(stocktag=stock.stocktag,
                        stockname=fields.pop(0),
                        qb9=fields.pop(0),
                        qb8=fields.pop(0),
                        qb7=fields.pop(0),
                        qb6=fields.pop(0),
                        qb5=fields.pop(0),
                        qb4=fields.pop(0),
                        qb3=fields.pop(0),
                        qb2=fields.pop(0),
                        qb1=fields.pop(0),)
                except:
                    log.append(stock)
    else:
        log.append('missing Object break!')
        print(log)
        return log
    log.append(len(log))
    return log


def update8(request,filename,obj):
    # print("如果要部分更新就寫這個function")
    # print(obj)
    # try:
    #     stocks=[]
    #     with open(filestr,'rt') as file:      
    #         lines=file.readlines()
    #         for line in lines[0:3]:
    #             fields=line.split(',')
    #             if fields:
    #                 stock=StockList.objects.get(stocktag=fields.pop(0))
    #                 print(fields)
    #                 stocks.append(stock)
    #                 obj.objects.stocktag=stock
    #                 obj.objects.stockname=fields.pop(0)
    #                 obj.objects.qb9=fields.pop(0)
    #                 obj.objects.qb8=fields.pop(0)
    #                 obj.objects.qb7=fields.pop(0)
    #                 obj.objects.qb6=fields.pop(0)
    #                 obj.objects.qb5=fields.pop(0)
    #                 obj.objects.qb4=fields.pop(0)
    #                 obj.objects.qb3=fields.pop(0)
    #                 obj.objects.qb2=fields.pop(0)
    #                 obj.objects.qb1=fields.pop(0)
    #                 print(obj.objects.stockname)
    #                 # obj.save()
    #                 print('5')
    #             # except:
    #                 # print('exception:'+str(stock))
    # except:
    #     print(stocks)
    #     return stocks.append(len(stocks))
    # print(stocks)
    return obj
# #------------------------------------------------------------
lmap9=[['variable',Tw50,'filename']]
lmap9.append(['dbr9',DebtsRatio9,'analysis/1-DebtsRatio9.csv'])
lmap9.append(['qkr9',QuickRatio9,'analysis/2-QuickRatio9.csv'])
lmap9.append(['gpm9',GPMargin9,'analysis/3-GPMargin9.csv'])
lmap9.append(['',Tw50,'analysis/4-.csv'])
lmap9.append(['opm9',OPMargin9,'analysis/5-OPMargin9.csv'])
lmap9.append(['npm9',NPMargin9,'analysis/6-NPMargin9.csv'])
lmap9.append(['roe9',ROE9,'analysis/7-ROE9.csv'])
lmap9.append(['rgq9',RevenueGrowthQoQ9,'analysis/8-RevenueGrowthQoQ9.csv'])
lmap9.append(['rgy9',RevenueGrowthYoY9,'analysis/9-RevenueGrowthYoY9.csv'])
lmap9.append(['epsfop9',EPSfromOP9,'analysis/10-EPSfromOP9.csv'])
lmap9.append(['epsatx9',EPSafterTax9,'analysis/11-EPSafterTax9.csv'])
lmap9.append(['epsytd9',EPSYTD9,'analysis/12-EPSYTD9.csv'])
lmap9.append(['pbr9',PBRatio9,'analysis/13-PBRatio9.csv'])
lmap9.append(['qesp9',QuarterEndStockPrice9,'analysis/14-QuarterEndStockPrice9.csv'])
lmap9.append(['bvps9',BVperShare9,'analysis/15-BVperShare9.csv'])
# #------------------------------------------------------------

def udfin9(request):
    #-----呼叫create9時會先清空原有資料 確認csv檔齊備後再作---
    list=[1,3,6,7,9,11,14,15]
    for i in list:
        log=create9(request,lmap9[i][2],lmap9[i][1])
    return HttpResponse(log)
#===============以下作市場交易資訊更新==============================================
import requests
from io import StringIO
import pandas as pd
import numpy as np
import time

def readmarket1(request):
    os.system('cls')
    time.sleep(3)
    d=str(datetime.datetime.now())
    datestr=d[0:4]+d[5:7]+d[8:10]
    # datestr="20181004"
    r = requests.post('http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + datestr + '&type=ALL')
    with open('analysis/twExchange.csv','wt') as file:
        l=file.write(r.text)
    log=datestr+' '+str(l)
    print(type(l))
    return HttpResponse(log)

def readmarket(request):
    log=[]
    db=mongoclient.midterm
    collection=db.MarketLogDs
    stocklist=StockList.objects.filter(selected=True)
    err=0
    #--------------------------循序上網擷取資料------------------
    for stock in stocklist:
        if err>=1:
            break
        if  collection.find_one({'stockname':stock.stockname}):
            pass
        else:
            try:
                #-----------狀態報告-----------
                log.append([stock.stocktag])
                print([stock.stocktag])
                #-------上網擷取資訊------------------
                time.sleep(random.uniform(1,3))
                twStock=twstock.Stock(stock.stocktag)
                #------------------------------------
            #     # obj=mld
            #     # obj=MarketLogD.objects.filter()
            # #     # clear=False
            # #     # if clear:
            # #     #     obj.delete()
            # #     #     log.append('檔案已清空')
            # #     #-------以上先把檔案清空------------
        
                downloaded={
                    'sid':twStock.sid,
                    'stockname':stock.stockname,
                    'date':twStock.date,
                    'open':twStock.open,
                    'high':twStock.high,
                    'low':twStock.low,
                    'close':twStock.close,
                    'change':twStock.change,
                    'capacity':twStock.capacity,
                    'turnover':twStock.turnover,
                    'transaction':twStock.transaction
                }
                collectone=collection.insert_one(downloaded)
            except:
                log.append('Error occured!')
                log.append('<br>')
                print('Error occured!')
                err+=1
                print(err)
    #----------擷取全部collection------
    mld=MarketLogD.objects.filter()
    mld.delete()
    i=0
    for doc in collection.find().sort('sid'):
        i+=1
        log.append('[{}]'.format(i))
        # log.append(doc['_id'])
        log.append(doc['sid'])
        log.append(doc['stockname'])
        log.append(doc['date'][-1])
        log.append(doc['close'][-1])
        log.append('<br>')
        #-----------寫入mySQL---------------
        # try:
        #     mld.create(
        #         stocktag=doc['sid'],
        #         # stockname=doc['stockname'],
        #         date=doc['date'][-1],
        #         open=doc['open'][-1],
        #         high=doc['high'][-1],
        #         low=doc['low'][-1],
        #         close=doc['close'][-1],
        #         change=doc['change'][-1],
        #         capacity=doc['capacity'][-1],
        #         turnover=doc['turnover'][-1],
        #         transaction=doc['transaction'][-1]
        #     )
        # except:
        #     pass
    #----------擷取特定一筆--------------
    # doc=collection.find_one(
    #         {'sid':'2301'}
    #     )
    # log.append(doc['_id'])
    # log.append(doc['sid'])
    # log.append(doc['stockname'])
    #----------修改特定一筆 尚未成功--------------
    # docs=collection.find(
    #         {'sid':'2301'}
    #     )
    # for doc in docs:
    #     stocklist=StockList.objects.get(stockname=doc['stockname'])
    #     log.append(stocklist.stocktag)
    #     log.append(stocklist.stockname)
    #     doc['sid']=stocklist.stocktag
    #     log.append(doc['sid'])
    #     doc.updateOne({'stockname':stocklist.stockname},{$set:{'sid':stocklist.stocktag}})    
    
    #-----------刪除特定一筆--------------
    # docs=collection.delete_one({'sid':'2301'})
    #------------------------------------
    # for i in range(3):,{sid:1,stockname:1}
    #     obj.create(stocktag=twStock.sid[i],
    #     stockname='',
    #     date=twStock.date[i],
    #     open=twStock.open[i],
    #     high=twStock.high[i],
    #     low=twStock.low[i],
    #     close=twStock.close[i],
    #     change=twStock.change[i],
    #     capacity=twStock.capacity[i],
    #     turnover=twStock.turnover[i],
    #     transaction=twStock.transaction[i])
    #     log.append(twStock.date[i])
    #     log.append(twStock.sid[i])
    #     log.append(twStock.close[i])
    #     mld.save()
    #     log.append(' ')
    #     stock.fetch_1()
    #     i=-1
    #     print(twStock.change[i])
    #     d={'sID':twStock.sid,'date':twStock.date[i],'open':twStock.open[i],'high':twStock.high[i],'low':twStock.low[i],'close':twStock.close[i],'change':twStock.change[i],'capacity':twStock.capacity[i],'turnover':twStock.turnover[i],'transaction':twStock.transaction[i]}
    # #     print(d)
    #     td={'sID':type(twStock.sid),'date':type(twStock.date[i]),'open':type(twStock.open[i]),'high':type(twStock.high[i]),'low':type(twStock.low[i]),'close':type(twStock.close[i]),'change':type(twStock.change[i]),'capacity':type(twStock.capacity[i]),'turnover':type(twStock.turnover[i]),'transaction':type(twStock.transaction[i])}
    # #     print(td)
    # print(twStock)
    # log.append(downloaded)
    # time.sleep(600)
    # readmarket(request)
    return HttpResponse(log)

def writemarket(request):
    # os.system('cls')
    # try:
    #     # twStock=twstock.DATATUPLE(datetime.datetime(2018, 10, 4, 0, 0))
    #     twStock=twstock.Stock('2301')
    #     i=29
    #     print(twStock.change[i])
    #     d={'sID':twStock.sid,'date':twStock.date[i],'open':twStock.open[i],'high':twStock.high[i],'low':twStock.low[i],'close':twStock.close[i],'change':twStock.change[i],'capacity':twStock.capacity[i],'turnover':twStock.turnover[i],'transaction':twStock.transaction[i]}
    #     print(d)
    #     td={'sID':type(twStock.sid),'date':type(twStock.date[i]),'open':type(twStock.open[i]),'high':type(twStock.high[i]),'low':type(twStock.low[i]),'close':type(twStock.close[i]),'change':type(twStock.change[i]),'capacity':type(twStock.capacity[i]),'turnover':type(twStock.turnover[i]),'transaction':type(twStock.transaction[i])}
    #     print(td)
    # except:
    #     pass
    # # log=twStock.codes
    # r = requests.post('http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + datestr + '&type=ALL')
    # with open('analysis/twExchange.csv','rt') as file:
    #     r=file.readline()
    # log.append(r.split(' ')[0])
    with open('analysis/twExchange.csv','rt') as file:
        r=file.read()
    df = pd.read_csv(StringIO("\n".join([i.translate({ord(c): None for c in ' '}) for i in r.split('\n') if len(i.split('",')) == 17 and i[0] != '='])), header=0)
    # "證券代號","證券名稱","成交股數","成交筆數","成交金額","開盤價","最高價","最低價","收盤價","漲跌(+/-)","漲跌價差","最後揭示買價","最後揭示買量","最後揭示賣價","最後揭示賣量","本益比",
 
    # log.append(df["成交股數"][0])
    log.append('<br>')
    log.append(int(df["證券代號"][939]))
    log.append('<br>')
    log.append(df["證券代號"].count())
    #------寫入mongodb的TPEXlogD------------------
    db=mongoclient.midterm
    collection=db.TPEXLogD
    # for i in range(df["證券代號"].count()):
    #     downloaded={
    #         'sid':df["證券代號"][i],
    #         'stockname':df["證券名稱"][i],
    #         'date':datetime.datetime.now(),
    #         'open':df["開盤價"][i],
    #         'high':df["最高價"][i],
    #         'low':df["最低價"][i],
    #         'close':df["收盤價"][i],
    #         'change':df["漲跌價差"][i],
    #         'capacity':df["成交股數"][i],
    #         'turnover':df["成交金額"][i],
    #         'transaction':df["成交筆數"][i]
    #     }
    #     collectione=collection.insert_one(downloaded)
    log.append('<br>')
    log.append(collection)
    log.append('<br>')
    log.append(collection.count())
    # # print(df.head(10))
    # print(df.ix)
    # print(df.columns)
    # print(df.shape)
    return HttpResponse(log)

def defaultwatchlist(request):
    wl=WatchList.objects.filter(accountId=0).order_by('group','index')
    #----------以下為尚未有watchlist時首度寫入----------
    # wl.delete()
    # group=1
    # index=1
    # for stock in StockList.objects.filter(selected=True):
    #     if group>3:
    #         break
    #     else:
    #         # wl.create(
    #         # email='visitor@iii',
    #         # group=group,
    #         # index=index,
    #         # stocktag=stock.stocktag,
    #         # stockname=stock.stockname,
    #         # date=datetime.datetime.now(),
    #         # accountId=0
    #         # )
    #         if index>5:
    #             group+=1
    #             index=1
    #         else:  
    #             index+=1
    for w in wl:
        log.append([w.group,w.index])
    return HttpResponse(log)

