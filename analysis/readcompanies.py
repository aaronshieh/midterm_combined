# import datetime
# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.db import connection
# from django.db import models
# from .models import StockList
# from django.core.files.storage import FileSystemStorage

# class StockList(models.Model):
#     stocktag=models.CharField(max_length=6,primary_key=True)
#     stockname=models.CharField(max_length=8)
#     industrySegment=models.CharField(max_length=8)
#     detailedSegment=models.CharField(max_length=8)
#     capitalsize=models.FloatField(max_length=12)
#     tw50=models.BooleanField()
#     mid100=models.BooleanField()
#     selectedlist=models.BooleanField()

#     def __str__(self):
#         return self.stocktag
#     class Meta:
#         managed = True
#         db_table='stocklist'
def readcom():
    with open('companyinfo.csv','rt') as file:
        lines=file.readlines()
        for line in lines:
            fields=line.split(',')
            print(fields)
        print(len(lines))

# st=StockList()
