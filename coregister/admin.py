from django.contrib import admin
from .models import User_data, Contact
# Register your models here.

@admin.register(User_data)
class User_dataAdmin(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'phone', 'email', 'age', 'blod', 'addres', 'state', 'city', 'zipcode', 'op_date', 'status']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['unique_id', 'name', 'phone', 'email', 'query']