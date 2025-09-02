from django.shortcuts import render
import requests
from .models import ConversaionHistory 

def convert_currancy(request):
    api_key = '135b44675282289494208c6e'
    api_url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'

    currencies = ['USD', 'AED', 'SAR', 'GBP', 'JPY']

    if request.method == 'POST':
        amount = float(request.POST.get('amount'))
        from_currency = request.POST.get('from_currency')
        to_currency = request.POST.get('to_currency')

        response = requests.get(api_url)
        data = response.json()

        if response.status_code == 200 and data['result'] == 'success':
            rates = data['conversion_rates']

            if from_currency in rates and to_currency in rates:
                converted_amount = amount * rates[to_currency] / rates[from_currency]

                # حفظ العملية
                ConversaionHistory.objects.create(
                    amount=amount,
                    from_currancy=from_currency,
                    to_currancy=to_currency,
                    converted_amount=converted_amount
                )

                context = {
                    'currencies': currencies,
                    'amount': amount,
                    'from_currency': from_currency,
                    'to_currency': to_currency,
                    'converted_amount': round(converted_amount, 2),
                    'history': ConversaionHistory.objects.all().order_by('-date')[:5]
                }
            else:
                context = {
                    'currencies': currencies,
                    'error': 'العملة غير مدعومة.'
                }
        else:
            context = {
                'currencies': currencies,
                'error': 'فشل جلب أسعار الصرف، نرجو المحاولة لاحقاً.'
            }
    else:
        context = {
            'currencies': currencies,
            'history': ConversaionHistory.objects.all().order_by('-date')[:5]
        }

    return render(request, 'converter.html', context)
