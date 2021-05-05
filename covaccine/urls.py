
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('coregister.urls')),
    path('', include('REST.urls')),
    path('', include('dashboard.urls')),
]
