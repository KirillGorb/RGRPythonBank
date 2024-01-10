from django.shortcuts import render, redirect
from .forms import LoginForm
from registration.models import User

def main_window(request):
    error = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone']
            user = User.objects.get(phone=phone_number)
            request.session['user_id'] = user.pk
            return redirect('account/')
        else:
            error = 'Форма была неверной'

    form = LoginForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'login/index.html', data)
