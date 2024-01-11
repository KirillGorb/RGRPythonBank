from django.shortcuts import render, redirect

from .forms import CategoriesForm
from service.forms import ServiceForm, CategoriesEnum

from service.models import Service
from .models import Treatys, Categories
from registration.models import User
from account.models import Account


def main_window(request):
    error = ''
    type = request.GET.get('value')

    if request.method == 'POST':
        service_form = ServiceForm(request.POST)
        categories_form = CategoriesForm(request.POST)

        if service_form.is_valid() and categories_form.is_valid():
            user = User.objects.get(pk=request.session.get('user_id'))

            account = Account.objects.get(user=user)
            account.invoice_size += service_form.cleaned_data['price']
            account.save()

            new_service = Service.objects.create(service=type, price=service_form.cleaned_data['price'],
                                                 yearly_percent=5)
            new_categories = Categories.objects.create(categorie=type,
                                                       time_active=categories_form.cleaned_data['time_active'],
                                                       service_id=new_service)
            Treatys.objects.create(client_id=user, service_id=new_categories)

            return redirect('account')
        else:
            error = 'Форма была неверной'

    service_form = ServiceForm()

    filtered_services = service_form.get_services(CategoriesEnum.CARD)
    if type == 'Кредит':
        filtered_services = service_form.get_services(CategoriesEnum.CREDIT)
    elif type == 'Ипотека':
        filtered_services = service_form.get_services(CategoriesEnum.MORTGAGE)
    elif type == 'Вклад':
        filtered_services = service_form.get_services(CategoriesEnum.DEPOSIT)

    categories_form = CategoriesForm()

    data = {
        'service_forms': filtered_services,
        'service_form': service_form,
        'categories_form': categories_form,
        'type': type,
        'error': error
    }

    return render(request, 'treaty/index.html', data)
