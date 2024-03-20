from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate,login,logout
class RegisterView(View):
    def get(self, request):
        form= RegisterForm()
        return render(request, 'users/register.html', context={'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('landing')
        else:
            return render(request, 'users/register.html', context={'form': form})
        
    
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', context={'form': form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('landing')

        # If form is not valid or user authentication fails
        return render(request, 'users/login.html', context={'form': form})
    


def profile(request):
    return render(request, 'users/profile.html')