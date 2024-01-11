from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_window, name='account'),
    path('payman/', views.payman_window, name='payman'),
    path('change/', views.change_window, name='change'),
    path('service_payment/', views.service_payment, name='service_payment')
]
