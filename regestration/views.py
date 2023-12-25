from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from regestration.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth
# Создаём функции для вывода html страницы
from django.urls import reverse

def regestration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('enterens'))
    else:
        form = UserRegistrationForm()
    
    context = {'form': form} 
    return render(request, 'regestration/regestration.html', context)


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


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            #update_session_auth_hash(request, user)  # Важно обновить хэш сессии
            return HttpResponseRedirect(reverse('profile'))  # Редирект на успешное изменение пароля
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password_change.html', {'form': form})