# set up django 
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StockProject.settings')
import django
django.setup()
# import imp modules
import pandas as pd
from baseApp.models import Sector, IndustrySector,Stock,DisplayStock

# read csv file
df_previous = pd.read_csv(r"C:\Users\Ashutosh Singh\Downloads\query-results.csv")
df = pd.read_csv(r"C:\Users\Ashutosh Singh\Downloads\query-results (1).csv")
#remove nan values
df = df.dropna()
df_previous = df_previous.dropna()

#collect what I want and convert them in a list object.
names = list(df['Name'])
industries = list(df['Industry'])

prices = list(df['Current Price'])
pre_prices = list(df_previous['Current Price'])

market_cap = list(df['Market Capitalization'])
bsc_code = list(df['BSE Code'])
nse_code = list(df['NSE Code'])

# store sectors

value = input('Want to edit sectors(yes/no): ')
if value == 'yes':
    for sector in industries:
        Sector.objects.get_or_create(name=sector)
    print('Sectors Updated successfully')

# store Industries
value = input('Want to edit industries(yes/no): ')
if value == 'yes':
    for industry in industries:
        sector = Sector.objects.get(name=industry)
        IndustrySector.objects.get_or_create(
            sector=sector, industry_name=industry)
    print('industries Updated successfully')
        
# Store Stocks
value = input('Want to edit Stocks(yes/no): ')
if value == 'yes':
    for name, bsc,nse,industry  in zip(names,bsc_code,nse_code,industries):
        industry=IndustrySector.objects.get(industry_name=industry)
        Stock.objects.get_or_create(industry=industry,stock_name=name,bse_code=bsc,nse_code=nse)
    print('Stocks Updated successfully')

# Daily wise data 
value = input('Want to edit Enter todays price(yes/no): ')
if value == 'yes':
    for name,c_price,p_price,market in zip(names,prices,pre_prices,market_cap):
        stock_name=Stock.objects.get(stock_name=name)
        DisplayStock.objects.create(name=stock_name,current_price=c_price,pre_price=p_price,market_cap=market)
        
    print('Prices Updated successfully')