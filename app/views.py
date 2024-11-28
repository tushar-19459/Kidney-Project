from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserSignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from .forms import UserSignUpForm

User = get_user_model()  # Get the user model (default or custom)

def signup_view(request):
    """View for user signup."""
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            return redirect('login')  # Redirect to login page after successful sign-up
    else:
        form = UserSignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    """View for user login."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Replace 'dashboard' with the name of your dashboard or home URL
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

@login_required
def logout_view(request):
    """View for user logout."""
    logout(request)
    return redirect('login')  # Redirect to login page after logging out
