from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
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


class SignUpForm(forms.ModelForm):
    username = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Логин', 'class': 'username'}))
    password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'class': 'password'}))
    password2 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder': 'Повтор пароля', 'class': 'password2'}))
    email = forms.EmailField(label=False, widget=forms.EmailInput(attrs={'placeholder': 'Почта', 'class': 'email'}))
    first_name = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'first_name'}))
    last_name = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Фамилия', 'class': 'last_name'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password2']
        
        
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password']:
            raise forms.ValidationError("Пароли не совпадают", code='password_mismatch')
        return cd['password']
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            self.add_error('email', forms.ValidationError("Такая почта уже существует"))
            self.fields['email'].widget.attrs.update({'class': 'err'})
        return email
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            self.add_error('username', forms.ValidationError("Такой логин уже существет"))
            self.fields['username'].widget.attrs.update({'class': 'err'})
        return username