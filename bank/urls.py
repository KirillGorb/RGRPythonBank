from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('account/', include('account.urls')),
    path('registration/', include('registration.urls')),
    path('service/', include('service.urls')),
    path('treaty/', include('treaty.urls'))
]
