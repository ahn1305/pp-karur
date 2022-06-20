from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import time
from django.urls import reverse


def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('hlb:home'))
    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            login(request,user)
            messages.success(request,"Registration Successful. ")
            return redirect("home")
        else: 
            messages.error(request,"Unsuccesful registration. Invalid information")
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {"register_form":form})
    

@login_required
def user_logout(request):
    time.sleep(2) # waiting for 2 sec
    logout(request) # using django.contrib.auth.logout(), It takes an HttpRequest object and has no return value
    messages.success(request,'You are logged out successfully') # logout success msg
    return redirect('users:login') # redirect to login page
