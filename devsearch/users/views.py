from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('edit-account')
        else:
            messages.error(request, 'Username OR password is incorrect')
    
    context = {
        'page': page,
    }        
    return render(request, 'users/login-register.html', context)


def regitsterUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created')

            login(request, user)
            return redirect('edit-account')
        else:
            messages.error(request, 'An error has occurred during registration')    

    context = {
        'page': page,
        'form': form,
    }   
    return render(request, 'users/login-register.html', context)


def logoutUser(request):
    logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect('login')


def profiles(request):
    profiles = Profile.objects.all()
    context = {
        'profiles': profiles,
    }
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact='')
    otherSkills = profile.skill_set.filter(description='')

    context = {
        'profile': profile,
        'topSkills': topSkills,
        'otherSkills': otherSkills,
    }
    return render(request, 'users/user-profile.html', context)
    

@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()

    context = {
        'profile': profile,
        'skills': skills,      
        'projects': projects
    }
    return render(request, 'users/account.html', context)   


@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid:
            form.save()

            return redirect('account')

    context = {
        'form': form,
    }
    return render(request, 'users/profile-form.html', context)