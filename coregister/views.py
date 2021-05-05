from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm, User_dataForm, ContactForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User_data, Contact
from django.contrib.auth.models import Group
import datetime

# Create your views here.

def Home(request):

    return render(request, 'home.html')

def About(request):

    return render(request, 'about.html')


def Report(request):
    posts = Contact.objects.all()
        
    return render(request, 'report.html', {'posts':posts})

def Cont_act(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                unique_id = form.cleaned_data['unique_id']
                name = form.cleaned_data['name']
                phone = form.cleaned_data['phone']
                email = form.cleaned_data['email']
                query = form.cleaned_data['query']
                post = Contact(unique_id=unique_id, name=name, phone=phone, email=email, query=query)
                post.save()
                form = ContactForm()
                messages.success(request, 'Admin will Respond you ASAP ...!!')
                return HttpResponseRedirect('/')
        else:
            form = ContactForm()
        return render(request, 'contact.html', {'form':form})
    else:
        messages.success(request, 'Please login ...!!')
        return HttpResponseRedirect('/login')
    


def Registration(request):
    if request.user.is_authenticated:
        posts = User_data.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request, 'Registration.html', {'posts':posts,'full_name':full_name, 'gps':gps})
    else:
        messages.success(request, 'Please login ...!!')
        return HttpResponseRedirect('/login')

def User_Signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Client')
            user.groups.add(group)
            messages.success(request, 'Successfully Created Please login ...!!')
            return HttpResponseRedirect('/login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form':form})

def User_Login(request):
    if not request.user.is_authenticated:
        if request.method =="POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Welcome Back...!!')
                    return HttpResponseRedirect('/Registration')
                else:
                    messages.success(request, 'Opps something has gone wrong !!!')
                    return HttpResponseRedirect('/login')
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form':form})
    else:
        messages.success(request, 'Already login ...!!')
        return HttpResponseRedirect('/Registration')

def User_Logout(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out ...!!')
    return HttpResponseRedirect('/')

def Register(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = User_dataForm(request.POST)
            if form.is_valid():
                fname = form.cleaned_data['fname']
                lname = form.cleaned_data['lname']
                phone = form.cleaned_data['phone']
                email = form.cleaned_data['email']
                age = form.cleaned_data['age']
                blod = form.cleaned_data['blod']
                addres = form.cleaned_data['addres']
                state = form.cleaned_data['state']
                city = form.cleaned_data['city']
                zipcode = form.cleaned_data['zipcode']
                Current_Date = datetime.datetime.now()
                op_date = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime('%y-%m-%d')
                status = 'waiting'
                post = User_data(fname=fname, lname=lname, phone=phone, email=email, age=age, blod=blod, addres=addres, state=state, city=city, zipcode=zipcode, op_date=op_date, status=status)
                post.save()
                form = User_dataForm()
                messages.success(request, "Registration Successfully your oppointment date is "+op_date)
                return HttpResponseRedirect('/')
        else:
            form = User_dataForm()
        return render(request, 'Register.html', {'form':form})
    else:
        messages.success(request, 'Please login.....!!')
        return HttpResponseRedirect('/login')

def Update(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = User_data.objects.get(pk=id)
            form = User_dataForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully Updated...!!')
                return HttpResponseRedirect('/Registration')
        else:
            obj = User_data.objects.get(pk=id)
            form = User_dataForm(instance=obj)
        return render(request, 'update.html', {'form':form})
    else:
        messages.success(request, 'Please login ...!!')
        return HttpResponseRedirect('/login')

def Delete(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = User_data.objects.get(pk=id)
            obj.delete()
            messages.success(request, 'Successfully Deleted...!!')
            return HttpResponseRedirect('/Registration')
        
        return render(request, 'Registration.html', {'form':form})
    else:
        messages.success(request, 'Please login ...!!')
        return HttpResponseRedirect('/login')