from django.db import models

# Create your models here.

class Sector(models.Model):
    name=models.CharField(max_length=150)



class IndustrySector(models.Model):
    sector=models.ForeignKey(Sector,on_delete=models.CASCADE)
    industry_name=models.CharField(max_length=150)


class Stock(models.Model):
    industry=models.ForeignKey(IndustrySector,on_delete=models.CASCADE)
    stock_name=models.CharField(max_length=150)
    market_cap=models.CharField(max_length=150,null=True,blank=True)
    bse_code=models.CharField(max_length=150)
    nse_code=models.CharField(max_length=150)

class StockData(models.Model):
    cob=models.DateField(auto_now=True)
    timestamp=models.DateTimeField(auto_now=True)
    stock=models.ForeignKey(Stock,on_delete=models.CASCADE)


class DisplayStock(models.Model):
    date=models.DateField(auto_now=True)
    name=models.ForeignKey(Stock,on_delete=models.CASCADE,null=True,blank=True)
    current_price=models.IntegerField()

    