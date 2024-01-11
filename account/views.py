from django.shortcuts import render, redirect
from treaty.models import Categories, Treatys
from service.models import Service
from registration.models import User
from .models import Account
from .forms import PayForm

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)


def main_window(request):
    user = User.objects.get(pk=request.session.get('user_id'))
    account = Account.objects.get(user=user)

    positiveTweet = [i * 5 for i in range(20)]
    youtube_video_id = 'https://youtu.be/8NdDwcXNwiA'
    context = {
        'youtube_video_id':youtube_video_id,
        'positiveTweet': positiveTweet,
        'account': account
    }
    return render(request, 'account/index.html', context)


def payman_window(request):
    error = ''
    if request.method == 'POST':
        form = PayForm(request.POST)
        if form.is_valid():
            pay = form.cleaned_data['invoice_size']
            user = User.objects.get(pk=request.session.get('user_id'))
            account = Account.objects.get(user=user)
            account.invoice_size+=pay
            account.save()
            return redirect('account')
        else:
            error = 'Форма была неверной'

    form = PayForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'account/payman.html', data)



def change_window(request):
    user = User.objects.get(pk=request.session.get('user_id'))
    account = Account.objects.get(user=user)
    treatys = Treatys.objects.filter(client_id=user)

    services = []

    for treaty in treatys:
        services.append(treaty.service_id.service_id)

    data = {
        'services': services,
        'account': account,
    }

    return render(request, 'account/cahnge.html', data)




def service_payment(request):
    index = request.GET.get('value')
    user = User.objects.get(pk=request.session.get('user_id'))
    account = Account.objects.get(user=user)

    service = Service.objects.get(id=index)

    if request.method == 'POST':
        formpay = PayForm(request.POST)
        if formpay.is_valid():
            pay = formpay.cleaned_data['invoice_size']
            if pay > service.price:
                account.invoice_size += (pay - service.price)
                service.delete()
            else:
                service.price -= pay
                service.save()
            account.invoice_size -= pay
            account.save()
            return redirect('account')

    formpay = PayForm()

    data = {
        'service': service,
        'account': account,
        'formpay': formpay,
    }

    return render(request, 'account/service_payment.html', data)





