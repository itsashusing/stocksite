from django.shortcuts import render
from baseApp.models import DisplayStock
from datetime import datetime, date

# Create your views here.


def HomeView(request):
    
    selected_date = DisplayStock.objects.values('date').distinct().last()
    selected_date = selected_date.get('date')

    price = request.GET.get('price')
    m_cap = request.GET.get('mcap')

    stockobj = DisplayStock.objects.all().order_by('-date').first()
    p_date = stockobj.date
    request.session['postdate']= p_date.isoformat()

    print(p_date)
    if request.method == 'POST':
        p_date = request.POST.get('dropdown')
        p_date = datetime.strptime(p_date, '%Y-%m-%d').date()

        request.session['postdate'] = p_date.isoformat()
        p_date = request.session.get('postdate')


        data = DisplayStock.objects.filter(date=p_date)

        return render(request, 'base/home.html', {'data': data[:50], 'p_date': p_date, 'price': price})

    elif price:
        p_date = request.session.get('postdate')
        data = DisplayStock.objects.filter(
            date=p_date).order_by('current_price')
    elif m_cap:
        p_date = request.session.get('postdate')
        data = DisplayStock.objects.filter(
            date=p_date).order_by('market_cap')
    else:
        data = DisplayStock.objects.filter(date=stockobj.date).order_by('-market_cap')
        p_date=stockobj.date

    request.session.set_expiry(300)

    context = {
        'data': data[:50],
        'p_date': p_date,
        'price': price,




    }

    return render(request, 'base/home.html', context=context)
