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
       
    
    
    
    class Meta:
        model = User
        fields = ("email", "image", "username")


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'confirm_password')
    
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Пароли не совпадают")
        return confirm_password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user