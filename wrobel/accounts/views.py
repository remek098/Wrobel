from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if(request.method == 'POST'):
        form = RegisterForm(request.POST)
        if form.is_valid(): 
            form.save()
            messages.success(request, f'Account created.')
            return redirect('login')

    else: 
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

def profile_update(request):
    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid:
            profile_form.save()
            return redirect('profile')
    else:
        profile_form = ProfileUpdateForm(instance=request.user.profile)


    return render(request, 'accounts/profile_update.html', {'profile_form':profile_form})