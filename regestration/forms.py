from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from regestration.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4",
        'placeholder': 'Введите логин'
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control py-4",
        'placeholder': "Введите пароль"
    }))
    
    class Meta:
        model = User
        fields = ('username', 'password')
        
        
class UserRegistrationForm(UserCreationForm):
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': "form-control py-4",
        'placeholder': 'Введите ваш электронный адрес'
    }))
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4",
        'placeholder': 'Введите логин'
    }))
    
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control py-4",
        'placeholder': "Введите пароль"
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control py-4",
        'placeholder': "Введите пароль ещё раз"
    }))    
       
    
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'username')    
        
        
class UserProfileForm(UserChangeForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': "form-control py-4",
        "readonly": True
    }))
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4",
        "readonly": True
    }))
    
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': "custom-file-input",
    }))
       
    
    
    
    class Meta:
        model = User
        fields = ("email", "image", "username")