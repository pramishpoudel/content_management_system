from django.shortcuts import render,redirect
from .forms import LoginForm,RegistrationForm,RecordForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .models import Record
# Create your views here.
def home(request):
    records= Record.objects.all()
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # return render(request, 'home.html')
                messages.success(request, 'You have been logged in successfully.')
                # Redirect to a success page.
                return redirect('home')
            else:
                messages.success(request, 'Invalid email or password.')
                return redirect('home')
                
        else:
            print(form.errors)
            # Add your authentication logic here
    return render(request,'home.html',{'records': records})


def login_view(request):
    form=LoginForm()
    return render(request,'home.html',{"form":form})


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')

    return render(request, 'home.html')


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            #for authenticating right after registration
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration successful. You can now log in.')
            return render(request, 'home.html')
        else:
            print(form.errors)
            form = RegistrationForm()
            return render(request, 'register.html', {'form': form})
    else:
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})


def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_record= Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, 'You must be logged in to view that page.')
        return redirect('home')

def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it= Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Record deleted successfully.')
        return redirect('home')
    else:
        messages.success(request, 'You must be logged in to do that.')
        return redirect('home')

def add_record(request):
    form=RecordForm()
    if request.method=='POST':
        form=RecordForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            phone=form.cleaned_data['phone']
            city=form.cleaned_data['city']
            country=form.cleaned_data['country']
            state=form.cleaned_data['state']
            zip_code=form.cleaned_data['zip_code']
            Record.objects.create(first_name=first_name,last_name=last_name,email=email,phone_number=phone,city=city,country=country,state=state,zip_code=zip_code)
            messages.success(request, 'Record added successfully.')
            return redirect('home')
    return render(request,'add_record.html',{'form':form})


def update_record(request,pk):
    record=Record.objects.get(id=pk)
    form=RecordForm(initial={
        'first_name':record.first_name,
        'last_name':record.last_name,
        'email':record.email,
        'phone':record.phone_number,
        'city':record.city,
        'country':record.country,
        'state':record.state,
        'zip_code':record.zip_code,
    })
    if request.method=='POST':
        form=RecordForm(request.POST)
        if form.is_valid():
            record.first_name=form.cleaned_data['first_name']
            record.last_name=form.cleaned_data['last_name']
            record.email=form.cleaned_data['email']
            record.phone_number=form.cleaned_data['phone']
            record.city=form.cleaned_data['city']
            record.country=form.cleaned_data['country']
            record.state=form.cleaned_data['state']
            record.zip_code=form.cleaned_data['zip_code']
            record.save()
            messages.success(request, 'Record updated successfully.')
            return redirect('home')
    return render(request,'update_record.html',{'form':form})