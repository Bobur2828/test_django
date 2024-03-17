from django import forms
from django.contrib.auth.models import User
class RegisterForm(forms.ModelForm):
    
    
    class Meta:
        model=User
        fields=('username', 'first_name', 'last_name','email', 'password')

class LoginForm(forms.Form):
    username = forms.CharField(label='Username kiriting')
    password = forms.CharField(label='Parolingizni kiriting',widget=forms.PasswordInput)