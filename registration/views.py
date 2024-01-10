from account.models import Account
from django.shortcuts import render, redirect
from .forms import UserForm  # Подставьте вашу форму для создания пользователя

def main_window(request):
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Account.objects.create(user=user, invoice_size=0)
            request.session['user_id'] = user.pk
            return redirect('account')
        else:
            error = 'Форма была неверной'

    form = UserForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'registration/index.html', data)
