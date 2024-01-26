from django.contrib import admin
from baseApp.models import Sector, Stock, StockData, IndustrySector,DisplayStock


class SectorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Sector, SectorAdmin)


class IndustrySectorAdmin(admin.ModelAdmin):
    list_display = ['id', 'sector', 'industry_name']


admin.site.register(IndustrySector, IndustrySectorAdmin)

class StockAdmin(admin.ModelAdmin):
    list_display=['id','stock_name','bse_code','nse_code']
admin.site.register(Stock,StockAdmin)
class DisplayStockAdmin(admin.ModelAdmin):
    list_display=['id','date','name','current_price']

admin.site.register(DisplayStock,DisplayStockAdmin)

admin.site.register(StockData)


# Register your models here.
