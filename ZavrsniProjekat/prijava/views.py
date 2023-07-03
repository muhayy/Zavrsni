from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .models import User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/home')  # Redirect to the appropriate page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print("Form data:", request.POST)  # Debugging statement
        print("Form errors:", form.errors)  # Debugging statement
        if form.is_valid():
            print("Form is valid")  # Debugging statement

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                User = get_user_model()
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                print("User does not exist:", username)  # Debugging statement
                return redirect('/home')

            if check_password(password, user.password):
                print("Password is correct")  # Debugging statement
                login(request, user)
                return redirect('/home')
            else:
                print("Invalid password")  # Debugging statement
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'account.html', {'form': form})

