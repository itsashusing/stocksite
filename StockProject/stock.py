# set up django 
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StockProject.settings')
import django
django.setup()
# import imp modules
import pandas as pd
from baseApp.models import Sector, IndustrySector,Stock,DisplayStock
from django.db import IntegrityError

# read csv file
df = pd.read_csv(r"C:\Users\Ashutosh Singh\Downloads\query-results (2).csv")
#remove nan values
df = df.dropna()


#collect what I want and convert them in a list object.
names = list(df['Name'])
industries = list(df['Industry'])

prices = list(df['Current Price'])

market_cap = list(df['Market Capitalization'])
bsc_code = list(df['BSE Code'])
nse_code = list(df['NSE Code'])

# store sectors
# DisplayStock.objects.all().delete()

value = input('Want to edit sectors(yes/no): ')
if value == 'yes':
    for sector in industries:
        Sector.objects.update_or_create(name=sector)
    print('Sectors Updated successfully')

# store Industries
value = input('Want to edit industries(yes/no): ')
if value == 'yes':
    for industry in industries:
        sector = Sector.objects.get(name=industry)
        IndustrySector.objects.update_or_create(
            sector=sector, industry_name=industry)
    print('industries Updated successfully')
        
# Store Stocks
value = input('Want to edit Stocks(yes/no): ')
if value == 'yes':
    for name, bsc,nse,industry  in zip(names,bsc_code,nse_code,industries):
        industry=IndustrySector.objects.get(industry_name=industry)
        try:
            Stock.objects.update_or_create(industry=industry,stock_name=name,bse_code=bsc,nse_code=nse)
        except IntegrityError:
            print(f'Stock {name} already exists and could not be updated.')
    print('Stocks Updated successfully')

# Daily wise data 
value = input('Want to edit Enter todays price(yes/no): ')
if value == 'yes':
    for name,c_price,market in zip(names,prices,market_cap):
        stock_name=Stock.objects.get(stock_name=name)
        print(str(stock_name.stock_name))
        DisplayStock.objects.create(name=stock_name,current_price=c_price,market_cap=market)
        
    print('Prices Updated successfully')