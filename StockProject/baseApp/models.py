from django.db import models
import PIL
# Create your models here.


class Sector(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self) :
        return f'({self.name})'

class IndustrySector(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    industry_name = models.CharField(max_length=150)

    def __str__(self) :
        return f'({self.industry_name})'

class Stock(models.Model):
    industry = models.ForeignKey(IndustrySector, on_delete=models.CASCADE,null=True,blank=True)
    stock_name = models.CharField(unique=True, max_length=150,null=True,blank=True)
    bse_code = models.CharField(unique=True, max_length=150,null=True,blank=True)
    nse_code = models.CharField(unique=True, max_length=150,null=True,blank=True)
    photo=models.ImageField(upload_to='static/images/',null=True,blank=True)

    def __str__(self) :
        return f'({self.stock_name})'

class StockData(models.Model):
    cob = models.DateField(auto_now=True)
    timestamp = models.DateTimeField(auto_now=True)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)


class DisplayStock(models.Model):
    date = models.DateField(auto_now=True)
    name = models.ForeignKey(Stock, on_delete=models.CASCADE)
    market_cap = models.FloatField()
    current_price = models.FloatField()

    def profit(self):
        stockpriceobj = DisplayStock.objects.filter(name=self.name,date__lt=self.date).order_by('-date').first()
      
        if stockpriceobj:
            pre_price = stockpriceobj.current_price
            current_price = self.current_price
            price = round(((current_price-pre_price)/pre_price)*100, 1)
            return price
        return None
