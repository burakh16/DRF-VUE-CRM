from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/account/', include('rest_auth.urls')),
    path('api/account/registration/', include('rest_auth.registration.urls')),

    path('admin/', admin.site.urls),
    path('api/', include('crm.routers')),
]
