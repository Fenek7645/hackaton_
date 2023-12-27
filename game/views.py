from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required



@login_required(login_url='')
def game(request):
    return render(request, 'test_game/main.html')




@login_required(login_url='')
def game1(request):
    return render(request, 'test_game/game1.html')


@login_required(login_url='')
def game1_1(request):
    return render(request, 'test_game/game1_1.html')


@login_required(login_url='')
def game1_2(request):
    return render(request, 'test_game/game1_2.html')

@login_required(login_url='')
def game1_3(request):
    return render(request, 'test_game/game1_3.html')

@login_required(login_url='')
def game2(request):
    return render(request, 'test_game/game2.html')

@login_required(login_url='')
def game3(request):
    return render(request, 'test_game/game3.html')

@login_required(login_url='')
def game4(request):
    return render(request, 'test_game/game4.html')

@login_required(login_url='')
def game5(request):
    return render(request, 'test_game/game5.html')

@login_required(login_url='')
def game6(request):
    return render(request, 'test_game/game6.html')

@login_required(login_url='')
def game7(request):
    return render(request, 'test_game/game7.html')

@login_required(login_url='')
def game8(request):
    return render(request, 'test_game/game8.html')

@login_required(login_url='')
def game9(request):
    return render(request, 'test_game/game9.html')

@login_required(login_url='')
def game10(request):
    return render(request, 'test_game/game10.html')
