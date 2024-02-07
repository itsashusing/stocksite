# set up django 
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StockProject.settings')
import django
django.setup()
# import imp modules
import pandas as pd
from baseApp.models import Sector, IndustrySector, Stock, DisplayStock
from django.db import IntegrityError

# read csv file
df = pd.read_csv(r"C:\Users\Ashutosh Singh\Downloads\query-results (1).csv")
# remove nan values
df = df.dropna()

# collect what I want and convert them into a list object.
names = list(df['Name'])
industries = list(df['Industry'])
prices = list(df['Current Price'])
market_cap = list(df['Market Capitalization'])
bsc_code = list(df['BSE Code'])
nse_code = list(df['NSE Code'])

# Limit to first 30 entries
names = names[:30]
industries = industries[:30]
prices = prices[:30]
market_cap = market_cap[:30]
bsc_code = bsc_code[:30]
nse_code = nse_code[:30]

# store sectors
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
    print('Industries Updated successfully')

# Store Stocks
value = input('Want to edit Stocks(yes/no): ')
if value == 'yes':
    folder_path='D:/photos_scarp/'
    for name, bsc, nse, industry ,filename in zip(names, bsc_code, nse_code, industries,os.listdir(folder_path)):
        industry = IndustrySector.objects.get(industry_name=industry)
        try:
            Stock.objects.get_or_create(industry=industry, stock_name=name, bse_code=bsc, nse_code=nse)

            if filename.endswith(('.jpg', '.jpeg', '.png')): 
                image_path = os.path.join(folder_path, filename)
                instance = Stock.objects.get(stock_name=name)

                with open(image_path, 'rb') as f:
                    instance.photo.save(os.path.basename(image_path), f, save=True)

        except IntegrityError:
            print(f'Stock {name} already exists and could not be updated.')
    print('Stocks Updated successfully')

# Daily wise data
value = input('Want to edit Enter today\'s price(yes/no): ')
if value == 'yes':
    for name, c_price, market in zip(names, prices, market_cap):
        stock_name = Stock.objects.get(stock_name=name)
        print(str(stock_name.stock_name))
        DisplayStock.objects.create(name=stock_name, current_price=c_price, market_cap=market)
    print('Prices Updated successfully')
