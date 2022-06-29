from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('store:index'))
    return render(request, 'accounts/login.html')


def logout_view(request):
    login_view(request)
    return redirect(reverse('store:index'))

def signup_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        return redirect(reverse('accounts:login'))
    return render(request, 'accounts/signup.html')

def profile_view(request):

    return render(request, 'accounts/accounts.html')