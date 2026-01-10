from django.shortcuts import render
from .forms import LoginForm,RegistrationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

# Create your views here.
def home(request):
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'home.html')
                # Redirect to a success page.
            else:
                messages.error(request, 'Invalid email or password.')
                
        else:
            print(form.errors)
            # Add your authentication logic here
    return render(request,'home.html',{'form': form})


def login_view(request):
    return render(request,'home.html',{})


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