from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from regestration.forms import UserLoginForm, CustomUserCreationForm, UserProfileForm
from django.contrib import auth
# Создаём функции для вывода html страницы
from django.urls import reverse

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            
            # Проверка на уникальность имени пользователя и email
            if User.objects.filter(username=username).exists():
                # Логин уже занят
                error_message = 'Этот логин уже занят.'
                return render(request, 'regestration/regestration.html', {'form': form, 'error_message': error_message})
            elif User.objects.filter(email=email).exists():
                # Email уже занят
                error_message = 'Эта почта уже занята.'
                return render(request, 'regestration/regestration.html', {'form': form, 'error_message': error_message})
            else:
                # Создание пользователя
                user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
                user.save()
                return redirect('login')  # Перенаправление на страницу входа после успешной регистрации
    else:
        form = CustomUserCreationForm()
    return render(request, 'regestration/regestration.html', {'form': form})



def enterens(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('profile'),)
            else:
                messages.error(request, 'Пожалуйста, проверьте введенные данные.')
    else:   
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'regestration/enterens.html', context)

@login_required(login_url='')
def profile(request):
    form = UserProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'regestration/profile.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            # Смена пароля
            request.user.set_password(password1)
            request.user.save()
            messages.success(request, 'Пароль успешно изменен.')
            return HttpResponseRedirect(reverse('profile'),)
        else:
            messages.error(request, 'Пароли не совпадают. Пожалуйста, попробуйте снова.')

    return render(request, 'password_change.html')
