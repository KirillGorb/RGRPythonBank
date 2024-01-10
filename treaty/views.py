from django.shortcuts import render, redirect
from .forms import CategoriesForm
from .models import Treatys
from service.forms import ServiceForm,Categories
from registration.models import User


def main_window(request):
    error = ''
    type = request.GET.get('value')

    if request.method == 'POST':
        service_form = ServiceForm(request.POST)
        categories_form = CategoriesForm(request.POST)

        if service_form.is_valid() and categories_form.is_valid():
            new_service = service_form.save(commit=False)
            new_service.yearly_percent = 5  # Устанавливаем годовой процент
            new_service.save()  # Сначала сохраняем объект Service

            new_categories = categories_form.save(commit=False)
            new_categories.service_id = new_service  # Используем сохраненный объект Service
            new_categories.categorie = type

            new_categories.save()  # Теперь сохраняем объект Categories

            user = User.objects.get(pk=request.session.get('user_id'))
            Treatys.objects.create(client_id=user, service_id=new_categories)

            return redirect('account')
        else:
            error = 'Форма была неверной'

    service_form = ServiceForm()

    filtered_services = service_form.get_services(Categories.CARD)
    if type == 'Кредит':
        filtered_services = service_form.get_services(Categories.CREDIT)
    elif type == 'Ипотека':
        filtered_services = service_form.get_services(Categories.MORTGAGE)
    elif type == 'Вклад':
        filtered_services = service_form.get_services(Categories.DEPOSIT)

    categories_form = CategoriesForm()

    data = {
        'service_forms': filtered_services,
        'service_form':service_form,
        'categories_form': categories_form,
        'type': type,
        'error': error
    }

    return render(request, 'treaty/index.html', data)
