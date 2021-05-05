from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import User_data, Contact

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'email')
        labels = {'first_name':'First Name', 'last_name':'Last Name', 'email':'Email',}
        widgets = {
        'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=_("password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))


class User_dataForm(forms.ModelForm):
    class Meta:
        model = User_data
        fields = ['fname', 'lname', 'phone', 'email', 'age', 'blod', 'addres', 'state', 'city', 'zipcode']
        labels = {'fname':'First Name', 'lname': 'Last Name','phone':'Phone no','email':'Email', 'age':'Age', 'blod':'Blood Group', 'state': 'State','city':'City','zipcode':'Zip Code'}
        widgets = {'fname':forms.TextInput(attrs={'class':'form-control','style': 'width:200px'}), 
        'lname':forms.TextInput(attrs={'class':'form-control','style': 'width:200px'}), 
        'phone':forms.NumberInput(attrs={'class':'form-control','style': 'width:200px'}),
        'email':forms.EmailInput(attrs={'class':'form-control','style': 'width:200px'}),
        'age':forms.NumberInput(attrs={'class':'form-control','style': 'width:200px'}),
        'blod':forms.TextInput(attrs={'class':'form-control','style': 'width:200px'}),
        'addres':forms.Textarea(attrs={'class':'form-control','style': 'width:300px;height:100px'}),
        'state':forms.TextInput(attrs={'class':'form-control','style': 'width:250px'}),
        'city':forms.TextInput(attrs={'class':'form-control','style': 'width:200px'}),
        'zipcode':forms.NumberInput(attrs={'class':'form-control','style': 'width:150px'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['unique_id', 'name','phone','email','query']
        labels = {'unique_id':'Unique ID', 'name':'Full Name','email':'Email ID','phone':'Phone No','query':'Discribe Problem'}
        widgets = {'unique_id':forms.NumberInput(attrs={'class':'form-control'}),
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        'phone':forms.NumberInput(attrs={'class':'form-control'}),
        'query':forms.Textarea(attrs={'class':'form-control'}),
        }

        # 'uni':forms.NumberInput(attrs={'class':'form-control'}),
        # 'name':forms.TextInput(attrs={'class':'form-control'}),
        # 'email':forms.EmailInput(attrs={'class':'form-control'}),
        # 'phone':forms.NumberInput(attrs={'class':'form-control'}),
        # 'query':forms.Textarea(attrs={'class':'form-control'}),