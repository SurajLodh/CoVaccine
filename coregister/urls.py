from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Home),
    path('about/', views.About, name='about'),
    path('contact/', views.Cont_act, name='contact'),
    path('Registration/', views.Registration, name='Registration'),
    path('logout/', views.User_Logout, name='logout'),
    path('signup/', views.User_Signup, name='signup'),
    path('login/', views.User_Login, name='login'),
    path('Register/', views.Register, name='Register'),
    path('update/<int:id>/', views.Update, name='update'),
    path('delete/<int:id>/', views.Delete, name='delete'),
    path('report/', views.Report, name='report'),
]