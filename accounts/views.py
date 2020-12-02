from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import User 
from .decorators import unauthenticated_user
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import ProfileForm

@unauthenticated_user
def RegisterUser(request):
    if request.method == 'POST':
        password = request.POST['password']
        passwordConfirm = request.POST['passwordConfirm']       
        email = request.POST['email']
        regCode = request.POST['regCode']
        if password==passwordConfirm:
            if regCode== 'enactusfudma':
                if User.objects.filter(email=email).exists():
                    messages.info(request, 'email taken')
                    return redirect('register')
                else:     
                    user = User.objects.create_user(password=password, email = email, regCode=regCode)
                    user.save();
                    messages.info(request, 'Registered Successfully')
                    return redirect('signin')
            else:
                messages.info(request, 'you have entered an incorrect reg code')
                return redirect('register')
        else:
            messages.info(request, 'password not match')
            return redirect('register')
        return redirect('/')
    else:        
        return render(request, 'accounts/register.html')

@unauthenticated_user
def LoginUser(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("profile")
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect ('signin')
    else:
        return render(request, 'accounts/login.html')

def logoutUser(request):
    logout(request)
    return redirect('signin')

def userProfile(request):
    return render(request, 'accounts/userprofile.html')

def AccountSettings(request):
    profile = request.user.profile 
    form = ProfileForm(instance=profile) 
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'accounts/accountsettings.html', context)

def Join(request):
    return render(request, 'pages/join_enactus.html')
