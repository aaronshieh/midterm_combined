from django.db import models

# Create your models here.
class StockList(models.Model):
    stocktag=models.CharField(max_length=6,primary_key=True)
    stockname=models.CharField(max_length=12)
    industry=models.CharField(max_length=20,blank=True,null=True)
    segment=models.CharField(max_length=20,blank=True,null=True)
    capital=models.FloatField(max_length=6,blank=True,null=True)
    tw50=models.NullBooleanField(blank=True,null=True)
    mid100=models.NullBooleanField(blank=True,null=True)
    selected=models.NullBooleanField(blank=True,null=True)
    watchlist1=models.NullBooleanField(blank=True,null=True)
    watchlist2=models.NullBooleanField(blank=True,null=True)
    watchlist3=models.NullBooleanField(blank=True,null=True)

    # def __str__(self):
    #     return self.stocktag
    # class Meta:
    #     managed = False
    #     ordering=['stocktag']
    #     db_table='stocklist'

class Tw50(models.Model):
    stocktag=models.CharField(max_length=6,primary_key=True)
    stockname=models.CharField(max_length=12)

    # def __str__(self):
    #     return self.stocktag
    # class Meta:
        # managed = False
        # ordering=['stocktag']
        # db_table='tw50'

class DebtsRatio9(models.Model):
    stocktag=models.CharField(max_length=6,primary_key=True)
    # stocktag=models.ForeignKey(StockList,models.DO_NOTHING,db_column='stocktag')
    stockname=models.CharField(max_length=12,blank=True,null=True)
    qb9=models.FloatField(max_length=5,blank=True,null=True)
    qb8=models.FloatField(max_length=5,blank=True,null=True)
    qb7=models.FloatField(max_length=5,blank=True,null=True)
    qb6=models.FloatField(max_length=5,blank=True,null=True)
    qb5=models.FloatField(max_length=5,blank=True,null=True)
    qb4=models.FloatField(max_length=5,blank=True,null=True)
    qb3=models.FloatField(max_length=5,blank=True,null=True)
    qb2=models.FloatField(max_length=5,blank=True,null=True)
    qb1=models.FloatField(max_length=5,blank=True,null=True)

    # def __str__(self):
    #     return self.stocktag
    # class Meta:
        # managed = False
        # ordering=['stocktag']
        # db_table='debtsratio9'
        
class QuickRatio9(models.Model):
    stocktag=models.CharField(max_length=6,primary_key=True)
    # stocktag=models.ForeignKey(StockList,models.DO_NOTHING,db_column='stocktag')
    stockname=models.CharField(max_length=12,blank=True,null=True)
    qb9=models.FloatField(max_length=5,blank=True,null=True)
    qb8=models.FloatField(max_length=5,blank=True,null=True)
    qb7=models.FloatField(max_length=5,blank=True,null=True)
    qb6=models.FloatField(max_length=5,blank=True,null=True)
    qb5=models.FloatField(max_length=5,blank=True,null=True)
    qb4=models.FloatField(max_length=5,blank=True,null=True)
    qb3=models.FloatField(max_length=5,blank=True,null=True)
    qb2=models.FloatField(max_length=5,blank=True,null=True)
    qb1=models.FloatField(max_length=5,blank=True,null=True)

    # def __str__(self):
    #     return self.stocktag
    # class Meta:
        # managed = False
        # ordering=['stocktag']
        # db_table='quickratio9'

class GPMargin9(models.Model):
    stocktag=models.CharField(max_length=6,primary_key=True)
    # stocktag=models.ForeignKey(StockList,models.DO_NOTHING,db_column='stocktag')
    stockname=models.CharField(max_length=12,blank=True,null=True)
    qb9=models.FloatField(max_length=5,blank=True,null=True)
    qb8=models.FloatField(max_length=5,blank=True,null=True)
    qb7=models.FloatField(max_length=5,blank=True,null=True)
    qb6=models.FloatField(max_length=5,blank=True,null=True)
    qb5=models.FloatField(max_length=5,blank=True,null=True)
    qb4=models.FloatField(max_length=5,blank=True,null=True)
    qb3=models.FloatField(max_length=5,blank=True,null=True)
    qb2=models.FloatField(max_length=5,blank=True,null=True)
    qb1=models.FloatField(max_length=5,blank=True,null=True)

    # def __str__(self):
    #     return self.stocktag
    # class Meta:
        # managed = False
        # ordering=['stocktag']
        # db_table='gpmargin9'

class OPMargin9(models.Model):
    stocktag=models.CharField(max_length=6,primary_key=True)
    # stocktag=models.ForeignKey(StockList,models.DO_NOTHING,db_column='stocktag')
    stockname=models.CharField(max_length=12,blank=True,null=True)
    qb9=models.FloatField(max_length=5,blank=True,null=True)
    qb8=models.FloatField(max_length=5,blank=True,null=True)
    qb7=models.FloatField(max_length=5,blank=True,null=True)
    qb6=models.FloatField(max_length=5,blank=True,null=True)
    qb5=models.FloatField(max_length=5,blank=True,null=True)
    qb4=models.FloatField(max_length=5,blank=True,null=True)
    qb3=models.FloatField(max_length=5,blank=True,null=True)
    qb2=models.FloatField(max_length=5,blank=True,null=True)
    qb1=models.FloatField(max_length=5,blank=True,null=True)

    # def __str__(self):
    #     return self.stocktag
    # class Meta:
        # managed = False
        # ordering=['stocktag']
        # db_table='opmargin9'

class NPMargin9(models.Model):
    stocktag=models.CharField(max_length=6,primary_key=True)
    # stocktag=models.ForeignKey(StockList,models.DO_NOTHING,db_column='stocktag')
    stockname=models.CharField(max_length=12,blank=True,null=True)
    qb9=models.FloatField(max_length=5,blank=True,null=True)
    qb8=models.FloatField(max_length=5,blank=True,null=True)
    qb7=models.FloatField(max_length=5,blank=True,null=True)
    qb6=models.FloatField(max_length=5,blank=True,null=True)
    qb5=models.FloatField(max_length=5,blank=True,null=True)
    qb4=models.FloatField(max_length=5,blank=True,null=True)
    qb3=models.FloatField(max_length=5,blank=True,null=True)
    qb2=models.FloatField(max_length=5,blank=True,null=True)
    qb1=models.FloatField(max_length=5,blank=True,null=True)

    # def __str__(self):
    #     return self.stocktag
    # class Meta:
        # managed = False
        # ordering=['stocktag']
        # db_table='npmargin9'
#-----------------------------------------------------------------------------------------
class ROE9(models.Model):
    stocktag=models.CharField(max_length=6,primary_key=True)
    # stocktag=models.ForeignKey(StockList,models.DO_NOTHING,db_column='stocktag')
    stockname=models.CharField(max_length=12,blank=True,null=True)
    qb9=models.FloatField(max_length=5,blank=True,null=True)
    qb8=models.FloatField(max_length=5,blank=True,null=True)
    qb7=models.FloatField(max_length=5,blank=True,null=True)
    qb6=models.FloatField(max_length=5,blank=True,null=True)
    qb5=models.FloatField(max_length=5,blank=True,null=True)
    qb4=models.FloatField(max_length=5,blank=True,null=True)
    qb3=models.FloatField(max_length=5,blank=True,null=True)
    qb2=models.FloatField(max_length=5,blank=True,null=True)
    qb1=models.FloatField(max_length=5,blank=True,null=True)

    # def __str__(self):
    #     return self.stocktag
    # class Meta:
        # managed = False
        # ordering=['stocktag']
        # db_table='roe9'
        
class RevenueGrowthQoQ9(models.Model):
    stocktag=models.CharField(max_length=6,primary_key=True)
    # stocktag=models.ForeignKey(StockList,models.DO_NOTHING,db_column='stocktag')
    stockname=models.CharField(max_length=12,blank=True,null=True)
    qb9=models.FloatField(max_length=5,blank=True,null=True)
    qb8=models.FloatField(max_length=5,blank=True,null=True)
    qb7=models.FloatField(max_length=5,blank=True,null=True)
    qb6=models.FloatField(max_length=5,blank=True,null=True)
    qb5=models.FloatField(max_length=5,blank=True,null=True)
    qb4=models.FloatField(max_length=5,blank=True,null=True)
    qb3=models.FloatField(max_length=5,blank=True,null=True)
    qb2=models.FloatField(max_length=5,blank=True,null=True)
    qb1=models.FloatField(max_length=5,blank=True,null=True)

    # def __str__(self):
    #     return self.stocktag
    # class Meta:
        # managed = False
        # ordering=['stocktag']
        # db_table='revenuegrowthqoq9'
        
class RevenueGrowthYoY9(models.Model):
    stocktag=models.CharField(max_length=6,primary_key=True)
    # stocktag=models.ForeignKey(StockList,models.DO_NOTHING,db_column='stocktag')
    stockname=models.CharField(max_length=12,blank=True,null=True)
    qb9=models.FloatField(max_length=5,blank=True,null=True)
    qb8=models.FloatField(max_length=5,blank=True,null=True)
    qb7=models.FloatField(max_length=5,blank=True,null=True)
    qb6=models.FloatField(max_length=5,blank=True,null=True)
    qb5=models.FloatField(max_length=5,blank=True,null=True)
    qb4=models.FloatField(max_length=5,blank=True,null=True)
    qb3=models.FloatField(max_length=5,blank=True,null=True)
    qb2=models.FloatField(max_length=5,blank=True,null=True)
    qb1=models.FloatField(max_length=5,blank=True,null=True)

    # def __str__(self):
    #     return self.stocktag
    # class Meta:
        # managed = False
        # ordering=['stocktag']
        # db_table='revenuegrowthyoy9'
        
class EPSfromOP9(models.Model):
    stocktag=models.CharField(max_length=6,primary_key=True)
    # stocktag=models.ForeignKey(StockList,models.DO_NOTHING,db_column='stocktag')
    stockname=models.CharField(max_length=12,blank=True,null=True)
    qb9=models.FloatField(max_length=5,blank=True,null=True)
    qb8=models.FloatField(max_length=5,blank=True,null=True)
    qb7=models.FloatField(max_length=5,blank=True,null=True)
    qb6=models.FloatField(max_length=5,blank=True,null=True)
    qb5=models.FloatField(max_length=5,blank=True,null=True)
    qb4=models.FloatField(max_length=5,blank=True,null=True)
    qb3=models.FloatField(max_length=5,blank=True,null=True)
    qb2=models.FloatField(max_length=5,blank=True,null=True)
    qb1=models.FloatField(max_length=5,blank=True,null=True)

    # def __str__(self):
    #     return self.stocktag
    # class Meta:
        # managed = False
        # ordering=['stocktag']
        # db_table='epsfromop9'
        
class EPSafterTax9(models.Model):
    stocktag=models.CharField(max_length=6,primary_key=True)
    # stocktag=models.ForeignKey(StockList,models.DO_NOTHING,db_column='stocktag')
    stockname=models.CharField(max_length=12,blank=True,null=True)
    qb9=models.FloatField(max_length=5,blank=True,null=True)
    qb8=models.FloatField(max_length=5,blank=True,null=True)
    qb7=models.FloatField(max_length=5,blank=True,null=True)
    qb6=models.FloatField(max_length=5,blank=True,null=True)
    qb5=models.FloatField(max_length=5,blank=True,null=True)
    qb4=models.FloatField(max_length=5,blank=True,null=True)
    qb3=models.FloatField(max_length=5,blank=True,null=True)
    qb2=models.FloatField(max_length=5,blank=True,null=True)
    qb1=models.FloatField(max_length=5,blank=True,null=True)

    # def __str__(self):
    #     return self.stocktag
    # class Meta:
        # managed = False
        # ordering=['stocktag']
        # db_table='epsaftertax9'

class EPSYTD9(models.Model):
    stocktag=models.CharField(max_length=6,primary_key=True)
    # stocktag=models.ForeignKey(StockList,models.DO_NOTHING,db_column='stocktag')
    stockname=models.CharField(max_length=12,blank=True,null=True)
    qb9=models.FloatField(max_length=5,blank=True,null=True)
    qb8=models.FloatField(max_length=5,blank=True,null=True)
    qb7=models.FloatField(max_length=5,blank=True,null=True)
    qb6=models.FloatField(max_length=5,blank=True,null=True)
    qb5=models.FloatField(max_length=5,blank=True,null=True)
    qb4=models.FloatField(max_length=5,blank=True,null=True)
    qb3=models.FloatField(max_length=5,blank=True,null=True)
    qb2=models.FloatField(max_length=5,blank=True,null=True)
    qb1=models.FloatField(max_length=5,blank=True,null=True)

    # def __str__(self):
    #     return self.stocktag
    # class Meta:
        # managed = False
        # ordering=['stocktag']
        # db_table='epsytd9'

class PBRatio9(models.Model):
    stocktag=models.CharField(max_length=6,primary_key=True)
    # stocktag=models.ForeignKey(StockList,models.DO_NOTHING,db_column='stocktag')
    stockname=models.CharField(max_length=12,blank=True,null=True)
    qb9=models.FloatField(max_length=5,blank=True,null=True)
    qb8=models.FloatField(max_length=5,blank=True,null=True)
    qb7=models.FloatField(max_length=5,blank=True,null=True)
    qb6=models.FloatField(max_length=5,blank=True,null=True)
    qb5=models.FloatField(max_length=5,blank=True,null=True)
    qb4=models.FloatField(max_length=5,blank=True,null=True)
    qb3=models.FloatField(max_length=5,blank=True,null=True)
    qb2=models.FloatField(max_length=5,blank=True,null=True)
    qb1=models.FloatField(max_length=5,blank=True,null=True)

    # def __str__(self):
    #     return self.stocktag
    # class Meta:
        # managed = False
        # ordering=['stocktag']
        # db_table='pbratio9'

class QuarterEndStockPrice9(models.Model):
    stocktag=models.CharField(max_length=6,primary_key=True)
    # stocktag=models.ForeignKey(StockList,models.DO_NOTHING,db_column='stocktag')
    stockname=models.CharField(max_length=12,blank=True,null=True)
    qb9=models.FloatField(max_length=5,blank=True,null=True)
    qb8=models.FloatField(max_length=5,blank=True,null=True)
    qb7=models.FloatField(max_length=5,blank=True,null=True)
    qb6=models.FloatField(max_length=5,blank=True,null=True)
    qb5=models.FloatField(max_length=5,blank=True,null=True)
    qb4=models.FloatField(max_length=5,blank=True,null=True)
    qb3=models.FloatField(max_length=5,blank=True,null=True)
    qb2=models.FloatField(max_length=5,blank=True,null=True)
    qb1=models.FloatField(max_length=5,blank=True,null=True)

    # def __str__(self):
    #     return self.stocktag
    # class Meta:
        # managed = False
        # ordering=['stocktag']
        # db_table='quarterendstockprice9'

class BVperShare9(models.Model):
    stocktag=models.CharField(max_length=6,primary_key=True)
    # stocktag=models.ForeignKey(StockList,models.DO_NOTHING,db_column='stocktag')
    stockname=models.CharField(max_length=12,blank=True,null=True)
    qb9=models.FloatField(max_length=5,blank=True,null=True)
    qb8=models.FloatField(max_length=5,blank=True,null=True)
    qb7=models.FloatField(max_length=5,blank=True,null=True)
    qb6=models.FloatField(max_length=5,blank=True,null=True)
    qb5=models.FloatField(max_length=5,blank=True,null=True)
    qb4=models.FloatField(max_length=5,blank=True,null=True)
    qb3=models.FloatField(max_length=5,blank=True,null=True)
    qb2=models.FloatField(max_length=5,blank=True,null=True)
    qb1=models.FloatField(max_length=5,blank=True,null=True)

    # def __str__(self):
    #     return self.stocktag
    # class Meta:
        # managed = False
        # ordering=['stocktag']
        # db_table='bvpershare9'

class MarketLogD(models.Model):
    # stocktag=models.CharField(max_length=6,primary_key=True )
    stocktag=models.ForeignKey(StockList,models.DO_NOTHING,db_column='stocktag',primary_key=True)
    # stockname=models.CharField(max_length=12,blank=True,null=True)
    date=models.DateTimeField(blank=True,null=True)
    open=models.FloatField(max_length=8,blank=True,null=True)
    high=models.FloatField(max_length=8,blank=True,null=True)
    low=models.FloatField(max_length=8,blank=True,null=True)
    close=models.FloatField(max_length=8,blank=True,null=True)
    change=models.FloatField(max_length=8,blank=True,null=True)
    capacity=models.IntegerField(blank=True,null=True)
    turnover=models.BigIntegerField(blank=True,null=True)
    transaction=models.IntegerField(blank=True,null=True)
#     # class Meta:
#         # managed = False
#         # db_table='marketlog'

class MarketLogDs(models.Model):
    stocktag=models.CharField(max_length=6)
    # tag=models.ForeignKey(Tw50,models.DO_NOTHING,db_column='stocktag')
    stockname=models.CharField(max_length=12,blank=True,null=True)
    date=models.DateTimeField(blank=True,null=True)
    open=models.FloatField(max_length=8,blank=True,null=True)
    high=models.FloatField(max_length=8,blank=True,null=True)
    low=models.FloatField(max_length=8,blank=True,null=True)
    close=models.FloatField(max_length=8,blank=True,null=True)
    change=models.FloatField(max_length=8,blank=True,null=True)
    capacity=models.IntegerField(blank=True,null=True)
    turnover=models.BigIntegerField(blank=True,null=True)
    transaction=models.IntegerField(blank=True,null=True)
    # class Meta:
        # managed = False
        # db_table='marketlog'


class WatchList(models.Model):
    accountId=models.IntegerField()
    email=models.EmailField(max_length=254,blank=True,null=True)
    group=models.IntegerField(max_length=2,blank=True,null=True)
    index=models.IntegerField(max_length=2,blank=True,null=True)
    stocktag=models.CharField(max_length=6,blank=True,null=True)
    # tag=models.ForeignKey(Tw50,models.DO_NOTHING,db_column='stocktag')
    stockname=models.CharField(max_length=12,blank=True,null=True)
    date=models.DateTimeField(blank=True,null=True)
    
#     # class Meta:
#         # managed = False
#         # db_table='marketlog'