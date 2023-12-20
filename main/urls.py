from django.urls import path
from . import views

# Здесть мы отслеживаем url адреса по которым переходит пользователь
urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path("chavo/", views.chavo, name="chavo")
]