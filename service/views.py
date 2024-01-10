from django.shortcuts import render, redirect

def main_window(request):
    if request.method == 'POST':
        value = request.POST.get('value')
        if value:
            request.session['type'] = value
            return redirect('treaty/')
    return render(request, 'service/index.html')
