import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StockProject.settings')
import django
django.setup()


import pandas as pd
from baseApp.models import Sector, IndustrySector,Stock,DisplayStock
df = pd.read_csv("C:\\Users\Ashutosh Singh\\Downloads\\query-results.csv")
df = df.dropna()
names = list(df['Name'])
industries = list(df['Industry'])
prices = list(df['Current Price'])
market_cap = list(df['Market Capitalization'])
bsc_code = list(df['BSE Code'])
nse_code = list(df['NSE Code'])


# for name,industry,price,market_cap,bsc,nse in zip(names[:10],industries[:10],prices[:10],market_cap[:10],bsc_id[:10],nse_id[:10]):
#     DisplayStock.objects.get_or_create(slug=name,name=name,price=price,industry=industry,market_cap=market_cap,bsc_code=bsc,nse_code=nse)

value = input('Want to edit sectors(yes/no): ')
if value == 'yes':
    for sector in industries:
        Sector.objects.get_or_create(name=sector)

value = input('Want to edit industries(yes/no): ')
if value == 'yes':
    for industry in industries:
        sector = Sector.objects.get(name=industry)
        IndustrySector.objects.get_or_create(
            sector=sector, industry_name=industry)
value = input('Want to edit Stocks(yes/no): ')
if value == 'yes':
    for name, bsc,nse,industry,market  in zip(names,bsc_code,nse_code,industries,market_cap):
        industry=IndustrySector.objects.get(industry_name=industry)
        Stock.objects.get_or_create(industry=industry,stock_name=name,bse_code=bsc,nse_code=nse,market_cap=market)
        

value = input('Want to edit Enter todays price(yes/no): ')
if value == 'yes':
    for name,price in zip(names,prices):
        stock_name=Stock.objects.get(stock_name=name)
        try:
            DisplayStock.objects.create(name=stock_name,current_price=price)
        except:
            DisplayStock.objects.create(name=None,current_price=price)