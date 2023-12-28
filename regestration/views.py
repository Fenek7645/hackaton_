from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from regestration.forms import UserLoginForm, SignUpForm, UserProfileForm
from django.contrib import auth, messages
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse
from django.http import HttpResponse, FileResponse
import os
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return HttpResponseRedirect(reverse('enterens'),)

    else:
        form = SignUpForm()
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
    access_granted = False
    if 'access_button' in request.GET and request.GET['access_button'] == 'true':
        access_granted = True

    form = UserProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'regestration/profile.html', {'access_granted': access_granted})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Обновляем сессионный ключ пользователя
            messages.success(request, 'Пароль успешно изменен!')
            return HttpResponseRedirect(reverse('profile'),)
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки ниже.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password_change.html', {'form': form})

@login_required
def download_file(request):
    # Путь к файлу, который вы хотите скачать
    file_path = 'hackaton/regestration/сертификат.pdf'  # Укажите путь к вашему файлу

    try:
        if os.path.exists(file_path):
            file = open(file_path, 'rb')
            response = FileResponse(file)
            response['Content-Disposition'] = 'attachment; filename="сертификат.pdf"'
            return response
        else:
            return HttpResponse('Файл не найден')
    except Exception as e:
        return HttpResponse(f'Произошла ошибка: {str(e)}')
    
    