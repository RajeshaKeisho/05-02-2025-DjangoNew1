from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import UserRegisterForm
from django.contrib.auth import views as auth_views
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your account has been created! You are now able to log in.')
            return redirect('login')      
    else:
        form = UserRegisterForm()
    return render(request, 'profiles/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return redirect('profiles/profile').url  
    
@login_required
def profile(request):
    return render(request, 'profiles/profile.html')

def custom_logout(request):
    messages.success(request, 'You have been successfully logged out.')
    return redirect('login')  
