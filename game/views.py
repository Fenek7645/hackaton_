from django.shortcuts import render
from django.contrib.auth.decorators import login_required



@login_required(login_url='')
def game(requset):
    return render(requset, 'test_game/main.html')