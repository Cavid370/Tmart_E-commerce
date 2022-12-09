from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
def register_view(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    context = {
        "form": form
    }
    return render(request,'registration/register.html', context)
def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(request, 
                                username = login_form.cleaned_data['username'], 
                                password = login_form.cleaned_data['password'])
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        login_form = LoginForm()
    context = {
        'form': login_form
    }
    return render(request,'registration/login.html',context)
@login_required
def profile_view(request):
    request.encoding = 'utf-8'
    context = {
        'user': request.user
    }
    return render(request, 'index.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')
    


