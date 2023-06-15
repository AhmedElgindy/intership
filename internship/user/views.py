from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegistrationForm
from .models import UserProfile
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def registerPatient(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            
            if password == confirm_password:
                user = form.save(commit=False)
                user.is_patient = True
                user.password = make_password(password)
                user.save()
                return render(request, 'login.html')
            else:
                form.add_error('confirm_password', 'Passwords do not match.')
    else:
        form = RegistrationForm()
    
    return render(request, 'registerPatient.html', {'form': form})

def registerDoctor(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            
            if password == confirm_password:
                user = form.save(commit=False)
                user.is_doctor = True
                user.password = make_password(password)
                user.save()
                return render(request, 'login.html')
            else:
                form.add_error('confirm_password', 'Passwords do not match.')
                print(form.errors)

    else:
        form = RegistrationForm()
    return render(request, 'registerDoctor.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_patient:
                login(request, user)
                return redirect(reverse('dashboard-patinet') + f'?user name={user.username}')
            elif user.is_doctor:
                login(request, user)
                return redirect(reverse('dashboard-doctor') + f'?user name={user.username}')
            else:
                messages.error(request, 'Invalid user type.')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')
    
@login_required(login_url='login')
def dashboardPatient(request):
    user_profile = request.user
    if user_profile.is_patient:
        return render(request, 'dashboardPatient.html', {'user_profile': user_profile})
    else:
        return redirect('login')  # Redirect to login if the user is not a patient

@login_required(login_url='login')
def dashboardDoctor(request):
    user_profile = request.user
    if user_profile.is_doctor:
        return render(request, 'dashboardDoctor.html', {'user_profile': user_profile})
    else:
        return redirect('login')  # Redirect to login if the user is not a doctor
