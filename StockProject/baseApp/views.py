from django.shortcuts import render
from baseApp.models import DisplayStock

# Create your views here.
def homeview(request):
    price= request.GET.get('price')
    m_cap=request.GET.get('mcap')
    if price:
        data=DisplayStock.objects.all().order_by('current_price')
    elif m_cap:
        data=DisplayStock.objects.all().order_by('name__market_cap')
    else:
        data=DisplayStock.objects.all()


    
    context={
        'data':data,
  
    }
    return render(request,'base/home.html',context=context)