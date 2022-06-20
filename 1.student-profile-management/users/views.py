from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            messages.success(request,'Registration Successful')
            return redirect('admin:index')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

