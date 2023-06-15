from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegistrationForm
from .models import UserProfile
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            return redirect(reverse('dashboard') + f'?username={user.username}')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('dashboard') + f'?username={user.username}')
        else:
            messages.error(request, 'Invalid username or password.')
            print("erorr in login")
            return redirect('login') 
    else:
        return render(request, 'login.html')
    
def dashboard(request):
    username = request.GET.get('username')
    if username:
        try:
            user_profile = UserProfile.objects.get(username=username)
            return render(request, 'dashboard.html', {'user_profile': user_profile})
        except UserProfile.DoesNotExist:
            messages.error(request, 'User not found.')
            return redirect('dashboard')
    return render(request, 'dashboard.html')

