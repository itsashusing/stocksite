from django.shortcuts import render
from baseApp.models import DisplayStock
from datetime import  datetime
# Create your views here.


def homeview(request):
    dateobject = DisplayStock.objects.values('date').distinct()
    price = request.GET.get('price')
    m_cap = request.GET.get('mcap')

    stockobj=DisplayStock.objects.all().order_by('-date').first()

    if request.method == 'POST':
        selected_date = request.POST.get('dropdown')
        selected_date = datetime.strptime(selected_date, '%b. %d, %Y').date()
        data = DisplayStock.objects.filter(date=selected_date)

        
    else:
        if price:
            data = DisplayStock.objects.filter(date=stockobj.date).order_by('current_price')
        elif m_cap:
            data = DisplayStock.objects.filter(date=stockobj.date).order_by('market_cap')
        else:
            data = DisplayStock.objects.filter(date=stockobj.date)


    context = {
        'data': data[:50],
        'dateobject': dateobject[::-1]

    }
    return render(request, 'base/home.html', context=context)


def lmarket_cap(request):
    dateobject = DisplayStock.objects.values('date').distinct()
    stockobj=DisplayStock.objects.all().order_by('-date').first()

    data = DisplayStock.objects.filter(date=stockobj.date).order_by('market_cap')
    context = {
        # 'data': data[:50],
        'dateobject': dateobject[::-1]

    }
    return render(request, 'base/home.html', context=context)

def rmarket_cap(request):
    dateobject = DisplayStock.objects.values('date').distinct()
    stockobj=DisplayStock.objects.all().order_by('-date').first()

    data = DisplayStock.objects.filter(date=stockobj.date).order_by('-market_cap')
    context = {
        # 'data': data[:50],
        'dateobject': dateobject[::-1]

    }
    return render(request, 'base/home.html', context=context)