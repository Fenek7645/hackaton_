from django.shortcuts import render

# Создаём функции для вывода html страницы

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html') 