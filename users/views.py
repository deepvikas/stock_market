from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import UserRegsiterForm


def register(request):
    if request.method == 'POST':
        form = UserRegsiterForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been Created! Please Login to Continue')
            return redirect('login')
    else:
        form = UserRegsiterForm()
    return render(request, 'users/register.html', {'form': form})