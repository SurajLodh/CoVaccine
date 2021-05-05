from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('api/data/', views.PersonView.as_view(), name='api-data'),
]